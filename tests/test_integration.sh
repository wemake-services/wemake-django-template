#!/usr/bin/env sh

set -o errexit
set -o nounset

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.

# Creating a test directory:
mkdir -p "$HOME/.test" && cd "$HOME/.test"

# Scaffold the project:
PROJECT_NAME='fake_project'
PROJECT_ORGANIZATION='wemake.services'

cookiecutter "$GITHUB_WORKSPACE" \
  --no-input --overwrite-if-exists \
  project_name="$PROJECT_NAME" \
  project_domain='myapp.com' \
  organization="$PROJECT_ORGANIZATION"

cd "$PROJECT_NAME"

# Run tests that are located inside the generate project:
docker-compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml config --quiet

# Buidling and testing dev image:
docker-compose build
docker-compose run --user=root --rm web ./docker/ci.sh

# Building and testing prod image:
docker-compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml build
docker-compose run --user=root --rm web \
  python manage.py check --deploy --fail-level WARNING

# Checking the size of final images:
disl "${PROJECT_NAME}:dev" 800MiB
disl "registry.gitlab.com/${PROJECT_ORGANIZATION}/${PROJECT_NAME}:latest" 600MiB
