#!/usr/bin/env sh

set -o errexit
set -o nounset

# Installing dependencies:
pipenv --bare install --dev --deploy

# Finding python installation:
VENV=$(pipenv --venv)

# Activating virtualenv:
echo "Activating $VENV ..."
. "$VENV/bin/activate"

# Running tests:
python -B -m pytest

# Running conditional commit lint:
LINT_COMMITS=${DOCKER_LINT_COMMITS:=true}

if "$LINT_COMMITS"; then
  printf "$(git log -1 --pretty=%B)" | python -m gitlint.cli
fi

# Running additional checks:
xenon --max-absolute B --max-modules A --max-average A .
pipenv check

# ---
# Generating reports as build artifacts, it will be possible
# to browse them later.

# Generating pylint report (it will have issues!):
PYLINT=$(find . -iname "*.py" | xargs pylint --reports=y || true)
echo "$PYLINT" > "pylint.rst"

# Generating code-quality report:
radon mi . > "mi.txt"

# Generating complexity report:
radon cc . --show-closures --total-average > "cc.txt"

# Generating raw metrics:
radon raw . > "raw.txt"
