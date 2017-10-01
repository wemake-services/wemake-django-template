# -*- coding: utf-8 -*-

"""
This file determines all the settings used in production.
This file is required and if development.py is present these
values are overridden.
"""

import os

from server.settings.components.common import BASE_DIR, CONFIG

# Production flags:

DEBUG = False

# Network security and SSL:

ALLOWED_HOSTS = [
    # TODO: check production hosts
    '{{ cookiecutter.project_domain }}',
]

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

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
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
