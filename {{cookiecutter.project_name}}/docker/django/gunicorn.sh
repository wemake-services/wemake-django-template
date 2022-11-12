#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $DJANGO_ENV is set to "production",
# fail otherwise, since it may break things:
echo "DJANGO_ENV is $DJANGO_ENV"
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
python /code/manage.py collectstatic --noinput --clear
python /code/manage.py compilemessages

# Precompress static files with brotli and gzip.
# The list of ignored file types was taken from https://github.com/evansd/whitenoise
find /var/www/django/static -type f \
  ! -regex '^.+\.\(jpg\|jpeg\|png\|gif\|webp\|zip\|gz\|tgz\|bz2\|tbz\|xz\|br\|swf\|flv\|woff\|woff2\|3gp\|3gpp\|asf\|avi\|m4v\|mov\|mp4\|mpeg\|mpg\|webm\|wmv\)$' \
  -exec brotli --force --best {} \+ \
  -exec gzip --force --keep --best {} \+

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
# Make sure it is in sync with `django/ci.sh` check:
/usr/local/bin/gunicorn \
  --config python:docker.django.gunicorn_config \
  server.wsgi
