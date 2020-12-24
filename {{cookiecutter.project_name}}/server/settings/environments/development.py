"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

import logging
from typing import List

from server.settings.components import config
from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
    'localhost',
    '0.0.0.0',  # noqa: S104
    '127.0.0.1',
    '[::1]',
]


# Installed apps for development only:

INSTALLED_APPS += (
    'debug_toolbar',
    'nplusone.ext.django',
    'django_migration_linter',
    'django_test_migrations.contrib.django_checks.AutoNames',
    'django_test_migrations.contrib.django_checks.DatabaseConfiguration',
    'extra_checks',
)


# Static files:
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS: List[str] = []


# Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # https://github.com/bradmontgomery/django-querycount
    # Prints how many queries were executed, useful for the APIs.
    'querycount.middleware.QueryCountMiddleware',
)


def _custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'server.settings.environments.development._custom_show_toolbar',
}

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
CSP_SCRIPT_SRC = ("'self'", 'ajax.googleapis.com')
CSP_IMG_SRC = ("'self'", 'data:')
CSP_CONNECT_SRC = ("'self'",)


# nplusone
# https://github.com/jmcarp/nplusone

# Should be the first in line:
MIDDLEWARE = (  # noqa: WPS440
    'nplusone.ext.django.NPlusOneMiddleware',
) + MIDDLEWARE

# Logging N+1 requests:
NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger('django')
NPLUSONE_LOG_LEVEL = logging.WARN
NPLUSONE_WHITELIST = [
    {'model': 'admin.*'},
]


# django-test-migrations
# https://github.com/wemake-services/django-test-migrations

# Set of badly named migrations to ignore:
DTM_IGNORED_MIGRATIONS = frozenset((
    ('axes', '*'),
))


# django-extra-checks
# https://github.com/kalekseev/django-extra-checks

EXTRA_CHECKS = {
    'checks': [
        # Forbid `unique_together`:
        'no-unique-together',
        # Require non empty `upload_to` argument:
        'field-file-upload-to',
        # Use the indexes option instead:
        'no-index-together',
        # Each model must be registered in admin:
        'model-admin',
        # FileField/ImageField must have non empty `upload_to` argument:
        'field-file-upload-to',
        # Text fields shouldn't use `null=True`:
        'field-text-null',
        # Prefer using BooleanField(null=True) instead of NullBooleanField:
        'field-boolean-null',
        # Don't pass `null=False` to model fields (this is django default)
        'field-null',
        # ForeignKey fields must specify db_index explicitly if used in
        # other indexes:
        {'id': 'field-foreign-key-db-index', 'when': 'indexes'},
        # If field nullable `(null=True)`,
        # then default=None argument is redundant and should be removed:
        'field-default-null',
        # Fields with choices must have companion CheckConstraint
        # to enforce choices on database level
        'field-choices-constraint',
    ],
}
