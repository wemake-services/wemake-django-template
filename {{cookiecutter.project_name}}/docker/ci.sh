#!/usr/bin/env sh

set -o errexit
set -o nounset

# Initializing global variables and functions:

: "${INSIDE_CI:=0}"
: "${DJANGO_ENV:='development'}"

# Fail CI if `DJANGO_ENV` is set to `production`:
if [ "$DJANGO_ENV" = 'production' ]; then
  echo 'DJANGO_ENV is set to production. Running tests is not safe.'
  exit 1
fi

pyclean () {
  # Cleaning cache:
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

run_ci () {
  # Running tests:
  mypy server tests
  pytest

  # Run checks to be sure settings are correct (production flag is required):
  DJANGO_ENV=production python /code/manage.py check \
    --deploy --fail-level WARNING

  # Check that all migrations worked fine:
  python /code/manage.py makemigrations --dry-run --check

  # Running code-quality check:
  xenon --max-absolute A --max-modules A --max-average A server

  # Checking docs:
  doc8 -q docs

  # Checking if all the dependencies are secure and do not have any
  # known vulnerabilities:
  pipenv check

  # Run this part only if truly inside the CI process:
  if [ "$INSIDE_CI" = 1 ]; then
    # Generating reports as build artifacts, it will be possible
    # to browse them later:
    # https://docs.gitlab.com/ce/user/project/pipelines/job_artifacts.html
    mkdir -p 'artifacts'

    # Generating pylint report (it will have issues!):
    # https://pylint.readthedocs.io/en/latest/
    PYLINT=$(pylint 'server' 'tests' || true)
    echo "$PYLINT" > 'artifacts/pylint.rst'

    # Generating code-quality report:
    # http://radon.readthedocs.io/en/latest/commandline.html
    radon mi . > 'artifacts/mi.txt'

    # Generating complexity report:
    radon cc . -s --show-closures --total-average > 'artifacts/cc.txt'

    # Generating raw metrics:
    radon raw . > 'artifacts/raw.txt'
  fi
}

install_deps () {
  # Installing dependencies:
  pipenv --bare install --system --dev --ignore-pipfile
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
install_deps
run_ci
