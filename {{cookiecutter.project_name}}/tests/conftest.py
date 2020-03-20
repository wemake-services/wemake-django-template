# -*- coding: utf-8 -*-

"""
This module is used to provide configuration, fixtures, and plugins for pytest.

It may be also used for extending doctest's context:
1. https://docs.python.org/3/library/doctest.html
2. https://docs.pytest.org/en/latest/doctest.html
"""

import pytest


@pytest.fixture(autouse=True)
def _media_root(settings, tmpdir_factory):
    """Forces django to save media files into temp folder."""
    settings.MEDIA_ROOT = tmpdir_factory.mktemp('media', numbered=True)


@pytest.fixture(autouse=True)
def _password_hashers(settings):
    """Forces django to use fast password hashers for tests."""
    settings.PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]


@pytest.fixture(autouse=True)
def _auth_backends(settings):
    """Deactivates security backend from Axes app."""
    settings.AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )


@pytest.fixture(autouse=True)
def _templates_debug(settings):
    """Activates TEMPLATE debug mode for coverage."""
    for template in settings.TEMPLATES:
        template['OPTIONS']['debug'] = True


@pytest.fixture()
def main_heading():
    """An example fixture containing some html fragment."""
    return '<h1>wemake-django-template</h1>'
