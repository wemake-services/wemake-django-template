#!/usr/bin/env sh

set -o errexit
set -o nounset

: ${INSIDE_CI:=0}
VIRTUAL_ENV_DISABLE_PROMPT=true

pyclean () {
  # Cleaning cache:
  find . | grep -E "(__pycache__|\.py[cod]$)" | xargs rm -rf
}

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

# Running additional checks:
xenon --max-absolute B --max-modules A --max-average A .
pipenv check

# Run this part only if truly inside the CI process:
if [[ "$INSIDE_CI" -eq 1 ]]; then
  # Running conditional commit lint:
  printf "$(git log -1 --pretty=%B)" | python -m gitlint.cli

  # Generating reports as build artifacts, it will be possible
  # to browse them later:
  # https://docs.gitlab.com/ce/user/project/pipelines/job_artifacts.html

  # Generating pylint report (it will have issues!):
  PYLINT=$(find . -iname "*.py" | xargs pylint --reports=y || true)
  echo "$PYLINT" > "artifacts/pylint.rst"

  # Generating code-quality report:
  radon mi . > "artifacts/mi.txt"

  # Generating complexity report:
  radon cc . --show-closures --total-average > "artifacts/cc.txt"

  # Generating raw metrics:
  radon raw . > "artifacts/raw.txt"
fi

# Clean everything up:
pyclean
