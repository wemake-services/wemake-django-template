#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

# Run checks to be sure everything will work fine:
python /code/manage.py check --deploy

# Run python specific scripts:
python /code/manage.py collectstatic --noinput
python /code/manage.py migrate --noinput

# Check that all migrations worked fine:
python /code/manage.py makemigrations --dry-run --check

# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn server.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/code
