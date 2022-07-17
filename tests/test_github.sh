#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.
. './tests/build.sh'

# Building the template:
run_cookiecutter_build "$GITHUB_WORKSPACE"
cd "$PROJECT_PATH"

# enable docker buildkit
export DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1

# Run tests that are located inside the generate project:
docker-compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml config --quiet

# Building and testing dev image:
docker-compose build
docker-compose run --user=root --rm web ./docker/ci.sh

# Building and testing prod image:
docker-compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml build
docker-compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml run \
  --user=root --rm web \
  python manage.py check --deploy --fail-level WARNING

# Checking the size of final images:
disl "${PROJECT_NAME}:dev" 950MiB
disl "registry.gitlab.com/${PROJECT_ORGANIZATION}/${PROJECT_NAME}:latest" 640MiB
