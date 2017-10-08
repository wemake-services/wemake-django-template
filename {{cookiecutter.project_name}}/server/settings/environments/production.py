# -*- coding: utf-8 -*-

"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""

import os

from server.settings.components.common import BASE_DIR

# Production flags:

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    '.{{ cookiecutter.project_url }}',
]


# Adding STATIC_ROOT to collect static files via 'collectstatic'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '{}.UserAttributeSimilarityValidator'.format(_PASS),
    },
    {
        'NAME': '{}.MinimumLengthValidator'.format(_PASS),
    },
    {
        'NAME': '{}.CommonPasswordValidator'.format(_PASS),
    },
    {
        'NAME': '{}.NumericPasswordValidator'.format(_PASS),
    },
]


# Security

SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'
