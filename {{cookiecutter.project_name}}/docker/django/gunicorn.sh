#!/usr/bin/env sh

set -o errexit
set -o nounset

# Check that $DJANGO_ENV is set to "production",
# fail otherwise, since it may break things:
echo "ENV is $DJANGO_ENV"
if [ "$DJANGO_ENV" != 'production' ]; then
  echo 'Error: DJANGO_ENV is not set to "production".'
  echo 'Application will not start.'
  exit 1
fi

export DJANGO_ENV

# Run checks to be sure everything will work fine:
python /code/manage.py check --deploy --fail-level WARNING

# Run python specific scripts:
python /code/manage.py migrate --noinput
python /code/manage.py collectstatic --noinput
python /code/manage.py compilemessages

# Check that all migrations worked fine:
python /code/manage.py makemigrations --dry-run --check

# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn server.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code
