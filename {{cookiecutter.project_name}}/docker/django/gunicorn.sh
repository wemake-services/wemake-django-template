#!/usr/bin/env sh

set -o errexit
set -o nounset

# Showing some information:
echo "ENV is $DJANGO_ENV"
export DJANGO_ENV

# Run checks to be sure everything will work fine:
python /code/manage.py check --deploy --fail-level WARNING

# Run python specific scripts:
python /code/manage.py collectstatic --noinput
python /code/manage.py migrate --noinput

# Check that all migrations worked fine:
python /code/manage.py makemigrations --dry-run --check

# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn server.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code
