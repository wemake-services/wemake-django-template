#!/usr/bin/env bash

# Used by both `test_github` and `test_gitlab`

set -o errexit
set -o nounset
set -o pipefail

# Creating a test directory:
readonly TEST_DIR='./.test'

# Scaffold the project:
readonly PROJECT_NAME='wemake-django-template'
readonly PROJECT_ORGANIZATION='sobolevn'

readonly PROJECT_PATH="$TEST_DIR/$PROJECT_NAME"

run_cookiecutter_build () {
  mkdir -p "$TEST_DIR" && cd "$TEST_DIR"

  cookiecutter "$1" \
    --no-input --overwrite-if-exists \
    project_name="$PROJECT_NAME" \
    project_domain='myapp.com' \
    organization="$PROJECT_ORGANIZATION"

  cd '..'
}

# Exporting variables:
export PROJECT_PATH
export PROJECT_NAME
export PROJECT_ORGANIZATION
