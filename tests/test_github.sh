#!/usr/bin/env sh

set -o errexit
set -o nounset

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.
. './tests/build.sh'

# Building the template:
run_cookiecutter_build "$GITHUB_WORKSPACE"
cd "$PROJECT_PATH"

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
disl "${PROJECT_NAME}:dev" 800MiB
disl "registry.gitlab.com/${PROJECT_ORGANIZATION}/${PROJECT_NAME}:latest" 600MiB
