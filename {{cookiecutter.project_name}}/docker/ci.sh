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
  # Running tests:
  mypy server
  pytest --dead-fixtures --dup-fixtures
  pytest

  # Run checks to be sure settings are correct (production flag is required):
  DJANGO_ENV=production python /code/manage.py check \
    --deploy --fail-level WARNING

  # Check that staticfiles app is working fine:
  DJANGO_ENV=production python manage.py collectstatic --no-input --dry-run

  # Check that all migrations worked fine:
  python /code/manage.py makemigrations --dry-run --check

  # Running code-quality check:
  xenon --max-absolute A --max-modules A --max-average A server

  # Checking if all the dependencies are secure and do not have any
  # known vulnerabilities:
  safety check --bare --full-report

  # Checking `pyproject.toml` file contents:
  poetry check

  # Checking docs:
  doc8 -q docs

  # Checking `yaml` files:
  yamllint -d '{"extends": "default", "ignore": ".venv"}' -s .
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_ci
