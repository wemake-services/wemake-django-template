# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import,unused-wildcard-import

"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

# Mind the proper import, use the right module!

from server.settings.components import GlobalIPList
from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE
from server.settings.environments.testing import *  # noqa

# Django debug toolbar:

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = GlobalIPList([
    '127.0.0.1',
    '10.0.2.2',

    # Uncomment next line and run 'runserver 0.0.0.0:8000'
    # for test purposes, you will need to modify the `net` part:
    # '192.168.net.*'
])
