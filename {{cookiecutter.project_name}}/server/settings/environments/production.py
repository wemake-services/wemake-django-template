"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""

from server.settings.components import config

# Production flags:
# https://docs.djangoproject.com/en/3.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config('DOMAIN_NAME'),

    # We need this value for `healthcheck` to work:
    'localhost',
]


# Staticfiles
# https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/

# This is a hack to allow a special flag to be used with `--dry-run`
# to test things locally.
_COLLECTSTATIC_DRYRUN = config(
    'DJANGO_COLLECTSTATIC_DRYRUN', cast=bool, default=False,
)
# Adding STATIC_ROOT to collect static files via 'collectstatic':
STATIC_ROOT = '.static' if _COLLECTSTATIC_DRYRUN else '/var/www/django/static'

STATICFILES_STORAGE = (
    # This is a string, not a tuple,
    # but it does not fit into 80 characters rule.
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)


# Media files
# https://docs.djangoproject.com/en/3.2/topics/files/

MEDIA_ROOT = '/var/www/django/media'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'  # noqa: S105
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS)},
    {'NAME': '{0}.MinimumLengthValidator'.format(_PASS)},
    {'NAME': '{0}.CommonPasswordValidator'.format(_PASS)},
    {'NAME': '{0}.NumericPasswordValidator'.format(_PASS)},
]


# Security
# https://docs.djangoproject.com/en/3.2/topics/security/

SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [
    # This is required for healthcheck to work:
    '^health/',
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
