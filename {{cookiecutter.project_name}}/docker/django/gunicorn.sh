#!/usr/bin/env sh

set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $DJANGO_ENV is set to "production",
# fail otherwise, since it may break things:
echo "ENV is $DJANGO_ENV"
if [ "$DJANGO_ENV" != 'production' ]; then
  echo 'Error: DJANGO_ENV is not set to "production".'
  echo 'Application will not start.'
  exit 1
fi

export DJANGO_ENV

# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/pages/template/production-checklist.rst
python /code/manage.py migrate --noinput
python /code/manage.py collectstatic --noinput
python /code/manage.py compilemessages

# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn server.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code
