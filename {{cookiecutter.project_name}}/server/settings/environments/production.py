# -*- coding: utf-8 -*-

"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""

from server.settings.components.common import config

# Production flags:

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config('DOMAIN_NAME'),
]


# Staticfiles
# https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/

# Adding STATIC_ROOT to collect static files via 'collectstatic'
STATIC_ROOT = '/var/www/django/static'

STATICFILES_STORAGE = (
    # This is a string, not a tuple,
    # but it does not fit into 80 characters rule.
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)


# Mediafiles
MEDIA_ROOT = '/var/www/django/media'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.MinimumLengthValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.CommonPasswordValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.NumericPasswordValidator'.format(_PASS),
    },
]


# Security
# https://docs.djangoproject.com/en/1.11/topics/security/

SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
