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

# Build docs
pwd
make -C docs html

# Move the result docs to the dest:
mv docs/_build ../..
