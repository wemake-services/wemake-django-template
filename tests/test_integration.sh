#!/usr/bin/env sh

set -o errexit
set -o nounset

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.

# Creating a test directory:
mkdir -p "$HOME/.test" && cd "$HOME/.test"

# Scaffold the project:
PROJECT_NAME="fake_project"

pipenv run cookiecutter "$TRAVIS_BUILD_DIR" \
  --no-input --overwrite-if-exists \
  project_name="$PROJECT_NAME" \
  project_url="myapp.com" \
  organization="wemake.services"

cd "$PROJECT_NAME"

# Run tests (without linting commits, since it is another repo):
docker-compose run -e INSIDE_CI=0 web ./docker/ci.sh
