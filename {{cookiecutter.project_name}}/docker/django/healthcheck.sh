#!/usr/bin/env sh

# We use full names of executables here,
# because k8s does not have `PATH` env var.
# This file is for our `docker` usage only, do not run it in local env.

set -o errexit
set -o nounset

/usr/bin/test "$(
  /usr/bin/curl 'http://localhost:8000/health/?format=json' \
  --fail \
  --write-out "%{http_code}" \
  --silent \
  --output /dev/null
)" -eq 200
/bin/echo 'ok'
