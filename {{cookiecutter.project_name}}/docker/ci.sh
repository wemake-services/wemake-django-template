#!/usr/bin/env sh

set -o errexit
set -o nounset

# Initializing global variables and functions:

: ${INSIDE_CI:=0}
: ${DJANGO_ENV:='development'}
VIRTUAL_ENV_DISABLE_PROMPT=true

pyclean () {
  # Cleaning cache:
  find . | grep -E '(__pycache__|\.py[cod]$)' | xargs rm -rf
}

# Fail CI if `DJANGO_ENV` is set to `production`:
if [[ "$DJANGO_ENV" == 'production' ]]; then
  echo 'DJANGO_ENV is set to production. Running tests is not safe.'
  exit 1
fi

# Installing dependencies:
pipenv --bare install --dev --deploy

# Finding python installation:
VENV=$(pipenv --venv)

# Activating virtualenv:
echo "Activating $VENV ..."
. "$VENV/bin/activate"

# Remove any cache before the script:
pyclean

# Running tests:
python -m mypy server
python -m pytest

# Running code-quality check:
xenon --max-absolute B --max-modules A --max-average A .

# Checking if all the dependencies are secure and do not have any
# known vulnerabilities:
pipenv check

# Run this part only if truly inside the CI process:
if [[ "$INSIDE_CI" -eq 1 ]]; then
  # Generating reports as build artifacts, it will be possible
  # to browse them later:
  # https://docs.gitlab.com/ce/user/project/pipelines/job_artifacts.html
  mkdir -p 'artifacts'

  # Generating pylint report (it will have issues!):
  # https://pylint.readthedocs.io/en/latest/
  PYLINT=$(find . -iname '*.py' | xargs pylint --reports=y || true)
  echo "$PYLINT" > 'artifacts/pylint.rst'

  # Generating code-quality report:
  # http://radon.readthedocs.io/en/latest/commandline.html
  radon mi . > 'artifacts/mi.txt'

  # Generating complexity report:
  radon cc . -s --show-closures --total-average > 'artifacts/cc.txt'

  # Generating raw metrics:
  radon raw . > 'artifacts/raw.txt'

  # Generating unused code report (it will have issues):
  # https://github.com/jendrikseipp/vulture
  VULTURE=$(vulture server tests --exclude server/settings/)
  echo "$VULTURE" > 'artifacts/vulture.txt'
fi

# Clean everything up:
pyclean
