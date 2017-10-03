#!/usr/bin/env sh

set -o errexit
set -o pipefail
set -o nounset

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.

# Installing dependencies:
pipenv --bare install --dev --deploy

# Finding python installation:
VENV=$(pipenv --venv)

# Activating virtualenv:
echo "Activating $VENV ..."
. "$VENV/bin/activate"

# Creating a test directory:
mkdir -p .cache/docker && cd .cache/docker

# Scaffold the project:
PROJECT_NAME="fake_project"

cookiecutter ../../ --no-input --overwrite-if-exists \
  project_name="$PROJECT_NAME" \
  project_url="myapp.com" \
  organization="wemake.services"

cd "$PROJECT_NAME"

# Run tests (without linting commits, since it is another repo):
docker-compose run web -e DOCKER_LINT_COMMITS=false ./docker/ci.sh
