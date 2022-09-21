#!/usr/bin/env sh

set -o errexit
set -o nounset


run_ci () {
  # Validating:
  caddy validate

  # Checking formatting:
  # TODO: we use this hack, because `caddy fmt` does not have `--check` arg.
  old_caddyfile="$(md5sum /srv/Caddyfile)"

  caddy fmt --overwrite

  if [ "$old_caddyfile" != "$(md5sum /srv/Caddyfile)" ]; then
    echo 'Invalid format'
    exit 1
  else
    echo 'Valid format'
  fi
}

# Run the CI process:
run_ci
