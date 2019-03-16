#!/usr/bin/env sh

set -o errexit
set -o nounset

# Initializing global variables and functions:
: "${DJANGO_ENV:=development}"

# Fail CI if `DJANGO_ENV` is not set to `development`:
if [ "$DJANGO_ENV" != 'development' ]; then
  echo 'DJANGO_ENV is not set to development. Running tests is not safe.'
  exit 1
fi

pyclean () {
  # Cleaning cache:
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

run_ci () {
  # Running linting for all python files in the project:
  flake8 **/*.py

  # Running tests and type checking:
  mypy server
  pytest --dead-fixtures --dup-fixtures
  pytest

  # Run checks to be sure settings are correct (production flag is required):
  DJANGO_ENV=production python manage.py check --deploy --fail-level WARNING

  # Check that staticfiles app is working fine:
  DJANGO_ENV=production python manage.py collectstatic --no-input --dry-run

  # Check that all migrations worked fine:
  python manage.py makemigrations --dry-run --check

  # Running code-quality check:
  xenon --max-absolute A --max-modules A --max-average A server

  # Checking if all the dependencies are secure and do not have any
  # known vulnerabilities:
  safety check --bare --full-report

  # Checking `pyproject.toml` file contents and dependencies status:
  poetry check && pip check

  # Checking docs:
  doc8 -q docs

  # Checking `yaml` files:
  yamllint -d '{"extends": "default", "ignore": ".venv"}' -s .

  # Checking `.env` files:
  dotenv-linter config/.env config/.env.template

  # Checking translation files, ignoring ordering and locations:
  polint -i location,unsorted locale
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_ci
