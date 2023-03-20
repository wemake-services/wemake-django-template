#!/usr/bin/env sh

set -o errexit
set -o nounset


run_ci () {
  # Validating:
  caddy validate --config /etc/caddy/Caddyfile

  # Checking formatting:
  # TODO: we use this hack, because `caddy fmt` does not have `--check` arg.
  old_caddyfile="$(md5sum /etc/caddy/Caddyfile)"

  caddy fmt --overwrite /etc/caddy/Caddyfile
 
  if [ "$old_caddyfile" != "$(md5sum /etc/caddy/Caddyfile)" ]; then
    echo 'Invalid format'
    exit 1
  else
    echo 'Valid format'
  fi
}

# Run the CI process:
run_ci
