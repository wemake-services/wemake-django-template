# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import,unused-wildcard-import

"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

from typing import List

from server.settings.components import GlobalIPList
from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


# Static files:
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS: List[str] = []


# Django debug toolbar
# django-debug-toolbar.readthedocs.io

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # https://github.com/bradmontgomery/django-querycount
    # Prints how many queries were executed, useful for the APIs.
    'querycount.middleware.QueryCountMiddleware',
)


def custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'server.settings.environments.development.custom_show_toolbar',
}

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
CSP_SCRIPT_SRC = ("'self'", 'ajax.googleapis.com')
CSP_IMG_SRC = ("'self'", 'data:')


# Internal IPs
# https://docs.djangoproject.com/en/1.11/ref/settings/#internal-ips

INTERNAL_IPS = GlobalIPList([
    '127.0.0.1',
    '10.0.2.2',

    # Uncomment next line and run 'runserver 0.0.0.0:8000'
    # for test purposes, you will need to modify the `net` part:
    # '192.168.net.*'
])
