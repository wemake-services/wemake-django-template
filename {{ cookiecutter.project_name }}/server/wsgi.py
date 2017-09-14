# -*- coding: utf-8 -*-

"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# To enable SSL add extra environment variables:
# os.environ['wsgi.url_scheme'] = 'https'
# os.environ['HTTPS'] = 'on'

application = get_wsgi_application()
