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
docker compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml config --quiet

# Building and testing dev image:
docker compose build --build-arg BUILDKIT_INLINE_CACHE=1
docker compose run --user=root --rm web ./docker/django/ci.sh

# Building and testing prod image:
docker compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml build
docker compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml run \
  --user=root --rm web \
  python manage.py check --deploy --fail-level WARNING

# Testing caddy configuration:
docker compose -f docker-compose.yml \
  -f docker/docker-compose.prod.yml run \
  --rm caddy sh /etc/ci.sh

# Checking the size of final images:
disl --current-size --max-layers=13 "${PROJECT_NAME}:dev" 950MiB
disl --current-size --max-layers=14 \
  "registry.gitlab.com/${PROJECT_ORGANIZATION}/${PROJECT_NAME}:latest" 700MiB
