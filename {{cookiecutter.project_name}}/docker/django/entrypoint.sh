#!/bin/sh

cmd="$@"

postgres_ready () {
  sh "/code/docker/django/wait-for-command.sh" -s 0 52 -c "curl db:5432"
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

# Evaluating passed command:
exec $cmd
