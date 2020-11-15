#!/usr/bin/env sh

set -o errexit
set -o nounset

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.
. './tests/build.sh'

# Building the template:
run_cookiecutter_build "$CI_PROJECT_DIR"
echo "Built $PROJECT_PATH"
