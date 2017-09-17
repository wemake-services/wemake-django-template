# -*- coding: utf-8 -*-

"""
This file determines all the settings that must define the development server.
Basically this is a local file. It is excluded from the VCS by default.

SECURITY WARNING: don't run with debug turned on in production!
"""

# Mind the proper import, use the right module!
# from server.settings.components.common import (
#     INSTALLED_APPS,
#     MIDDLEWARE_CLASSES,
# )

# Setting the development status:

DEBUG = True

FRONTEND_DEBUG = True

# Network security and SSL:

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',

    # Uncomment next line and run 'runserver 0.0.0.0:8000' for production test:
    # '192.168.your.ip'
]

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False


# Static files:
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS = []
