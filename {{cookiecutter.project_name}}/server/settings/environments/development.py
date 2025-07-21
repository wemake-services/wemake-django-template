"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

from __future__ import annotations

import logging
import socket
from typing import TYPE_CHECKING

from server.settings.components import config
from server.settings.components.common import (
    DATABASES,
    INSTALLED_APPS,
    MIDDLEWARE,
)
from server.settings.components.csp import (
    CSP_CONNECT_SRC,
    CSP_IMG_SRC,
    CSP_SCRIPT_SRC,
)

if TYPE_CHECKING:
    from django.http import HttpRequest

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
    # Better debug:
    'debug_toolbar',
    'zeal',
    # Linting migrations:
    'django_migration_linter',
    # django-test-migrations:
    'django_test_migrations.contrib.django_checks.AutoNames',
    # This check might be useful in production as well,
    # so it might be a good idea to move `django-test-migrations`
    # to prod dependencies and use this check in the main `settings.py`.
    # This will check that your database is configured properly,
    # when you run `python manage.py check` before deploy.
    'django_test_migrations.contrib.django_checks.DatabaseConfiguration',
    # django-extra-checks:
    'extra_checks',
    # django-query-counter:
    'query_counter',
    # django-drifter:
    'drifter',
)


# Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # https://github.com/conformist-mw/django-query-counter
    # Prints how many queries were executed, useful for the APIs.
    'query_counter.middleware.DjangoQueryCounterMiddleware',
)

# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#configure-internal-ips
try:  # This might fail on some OS
    INTERNAL_IPS = [
        '{}.1'.format(ip[: ip.rfind('.')])
        for ip in socket.gethostbyname_ex(socket.gethostname())[2]
    ]
except OSError:  # pragma: no cover
    INTERNAL_IPS = []
INTERNAL_IPS += ['127.0.0.1', '10.0.2.2']


def _custom_show_toolbar(request: HttpRequest) -> bool:
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': (
        'server.settings.environments.development._custom_show_toolbar'
    ),
}

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
CSP_SCRIPT_SRC += ('ajax.googleapis.com',)
CSP_IMG_SRC += ('data:',)
CSP_CONNECT_SRC += ("'self'",)


# django-zeal
# https://github.com/taobojlen/django-zeal

# Should be the first in line:
MIDDLEWARE = ('zeal.middleware.zeal_middleware', *MIDDLEWARE)

# Logging N+1 requests:
ZEAL_RAISE = True  # comment out if you want to allow N+1 requests
ZEAL_SHOW_ALL_CALLERS = True
ZEAL_LOGGER = logging.getLogger('django')
ZEAL_ALLOWLIST = [
    {'model': 'admin.*'},
]


# django-test-migrations
# https://github.com/wemake-services/django-test-migrations

# Set of badly named migrations to ignore:
DTM_IGNORED_MIGRATIONS = frozenset((('axes', '*'),))


# django-migration-linter
# https://github.com/3YOURMIND/django-migration-linter

MIGRATION_LINTER_OPTIONS = {
    'exclude_apps': ['axes'],
    'exclude_migration_tests': ['CREATE_INDEX', 'CREATE_INDEX_EXCLUSIVE'],
    'warnings_as_errors': True,
}


# django-extra-checks
# https://github.com/kalekseev/django-extra-checks

EXTRA_CHECKS = {
    'checks': [
        # Forbid `unique_together`:
        'no-unique-together',
        # Each model must be registered in admin:
        'model-admin',
        # FileField/ImageField must have non empty `upload_to` argument:
        'field-file-upload-to',
        # Text fields shouldn't use `null=True`:
        'field-text-null',
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

# Disable persistent DB connections
# https://docs.djangoproject.com/en/5.2/ref/databases/#caveats
DATABASES['default']['CONN_MAX_AGE'] = 0
