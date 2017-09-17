# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import,unused-wildcard-import

"""
This file determines all the settings that must define the development server.
Basically this is a local file. It is excluded from the VCS by default.

SECURITY WARNING: don't run with debug turned on in production!
"""

# Mind the proper import, use the right module!

from server.settings.components import GlobalIPList
from server.settings.environments.testing import *  # NOQA

INTERNAL_IPS = GlobalIPList([
    '127.0.0.1',

    # Uncomment next line and run 'runserver 0.0.0.0:8000' for production test:
    # '192.168.net.*'
])
