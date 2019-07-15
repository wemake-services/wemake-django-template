# -*- coding: utf-8 -*-

"""
This module is called after project is created.

It does the following:
1. Generates and saves random secret key
2. Removes docker files if it is not used

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
https://github.com/django/django/blob/master/django/utils/crypto.py

And from pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os
import secrets
import shutil
import string

# CHANGEME mark
CHANGEME = '__CHANGEME__'

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = '{{ cookiecutter.project_name }}'


def _get_random_string(length=50):
    """
    Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    punctuation = string.punctuation.replace(
        '"', '',
    ).replace(
        "'", '',
    ).replace(
        '\\', '',
    ).replace(
        '$', '',  # see issue-271
    )

    chars = string.digits + string.ascii_letters + punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def _create_secret_key(config_path):
    with open(config_path) as config_file:
        file_contents = config_file.read()

    # Generate a SECRET_KEY that matches the Django standard
    secret_key = _get_random_string()

    # Replace CHANGEME with SECRET_KEY
    file_contents = file_contents.replace(CHANGEME, secret_key, 1)

    # Write the results to the file
    with open(config_path, 'w') as config_file:
        config_file.write(file_contents)


def print_futher_instuctions():
    """Shows user what to do next after project creation."""
    print()
    print('Your project {0} is created.'.format(PROJECT_NAME))
    print('Now you can start working on it:')
    print()
    print('    cd {0}'.format(PROJECT_NAME))


def copy_local_configuration():
    """
    Handler to copy local configuration.

    It is copied from ``.template`` files to the actual files.
    """
    secret_template = os.path.join(
        PROJECT_DIRECTORY, 'config', '.env.template',
    )
    secret_config = os.path.join(
        PROJECT_DIRECTORY, 'config', '.env',
    )
    shutil.copyfile(secret_template, secret_config)
    _create_secret_key(secret_config)

    # Local config:
    local_template = os.path.join(
        PROJECT_DIRECTORY,
        'server',
        'settings',
        'environments',
        'local.py.template',
    )
    local_config = os.path.join(
        PROJECT_DIRECTORY,
        'server',
        'settings',
        'environments',
        'local.py',
    )
    shutil.copyfile(local_template, local_config)


copy_local_configuration()
print_futher_instuctions()
