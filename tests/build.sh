#!/usr/bin/env sh

set -o errexit
set -o nounset

# Creating a test directory:
readonly TEST_DIR=".test"

# Scaffold the project:
readonly PROJECT_NAME='fake_project'
readonly PROJECT_ORGANIZATION='wemake.services'

readonly PROJECT_PATH="$TEST_DIR/$PROJECT_NAME"

run_cookiecutter_build () {
  mkdir -p "$TEST_DIR" && cd "$TEST_DIR"

  cookiecutter "$1" \
    --no-input --overwrite-if-exists \
    project_name="$PROJECT_NAME" \
    project_domain='myapp.com' \
    organization="$PROJECT_ORGANIZATION"
}

# Exporting variables:
export PROJECT_PATH
export PROJECT_NAME
export PROJECT_ORGANIZATION
