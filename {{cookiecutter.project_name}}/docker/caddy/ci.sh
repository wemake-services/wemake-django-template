#!/usr/bin/env sh

set -o errexit
set -o nounset

CADDYFILE_PATH='/etc/caddy/Caddyfile'

run_ci () {
  # Validating:
  caddy validate --config "$CADDYFILE_PATH"

  # Checking formatting:
  # TODO: we use this hack, because `caddy fmt` does not have `--check` arg.
  old_caddyfile="$(md5sum "$CADDYFILE_PATH")"

  caddy fmt --overwrite "$CADDYFILE_PATH"

  if [ "$old_caddyfile" != "$(md5sum "$CADDYFILE_PATH")" ]; then
    echo 'Invalid format'
    exit 1
  else
    echo 'Valid format'
  fi
}

# Run the CI process:
run_ci
