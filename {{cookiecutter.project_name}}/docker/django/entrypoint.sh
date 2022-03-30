#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

readonly cmd="$*"

: "${DJANGO_DATABASE_HOST:=db}"
: "${DJANGO_DATABASE_PORT:=5432}"

# We need this line to make sure that this container is started
# after the one with postgres:
dockerize \
  -wait "tcp://${DJANGO_DATABASE_HOST}:${DJANGO_DATABASE_PORT}" \
  -timeout 90s

# It is also possible to wait for other services as well: redis, elastic, mongo
>&2 echo 'Postgres is up - continuing...'

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd
