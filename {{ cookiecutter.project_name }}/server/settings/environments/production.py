# -*- coding: utf-8 -*-

"""
This file determines all the settings used in production.
This file is required and if development.py is present these
values are overridden.
"""

import os

from server.settings.components.common import BASE_DIR

# Production flags:

DEBUG = False

# Network security and SSL:

ALLOWED_HOSTS = [
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
