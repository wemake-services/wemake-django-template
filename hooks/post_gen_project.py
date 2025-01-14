"""
This module is called after project is created.

It does the following:
1. Generates and saves random secret key
2. Prints further instructions

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
https://github.com/django/django/blob/master/django/utils/crypto.py

And from pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import secrets
import shutil
import string
from pathlib import Path
from typing import Final

# CHANGEME mark
CHANGEME: Final = '__CHANGEME__'

# Get the root project directory
PROJECT_DIRECTORY: Final = Path.cwd().resolve(strict=True)
PROJECT_NAME: Final = '{{ cookiecutter.project_name }}'

# Messages
PROJECT_SUCCESS: Final = """
Your project {0} is created.
Now you can start working on it:

    cd {0}
"""


def _get_random_string(length: int = 50) -> str:
    """
    Returns a securely generated random string.

    >>> secret = _get_random_string()
    >>> len(secret)
    50

    """
    punctuation = (
        string.punctuation.replace(
            '"',
            '',
        )
        .replace(
            "'",
            '',
        )
        .replace(
            '\\',
            '',
        )
        .replace(
            '$',
            '',  # see issue-271
        )
    )

    chars = string.digits + string.ascii_letters + punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def _create_secret_key(config_path: Path) -> None:
    # Generate a SECRET_KEY that matches the Django standard
    secret_key = _get_random_string()

    with config_path.open(mode='r+', encoding='utf8') as config_file:
        # Replace CHANGEME with SECRET_KEY
        file_contents = config_file.read().replace(CHANGEME, secret_key, 1)

        # Write the results to the file:
        config_file.seek(0)
        config_file.write(file_contents)
        config_file.truncate()


def print_futher_instuctions() -> None:
    """Shows user what to do next after project creation."""
    print(PROJECT_SUCCESS.format(PROJECT_NAME))  # noqa: WPS421


def copy_local_configuration() -> None:
    """
    Handler to copy local configuration.

    It is copied from ``.template`` files to the actual files.
    """
    secret_template = PROJECT_DIRECTORY / 'config' / '.env.template'
    secret_config = PROJECT_DIRECTORY / 'config' / '.env'
    shutil.copyfile(secret_template, secret_config)
    _create_secret_key(secret_config)

    # Local config:
    local_template = (
        PROJECT_DIRECTORY
        / 'server'
        / 'settings'
        / 'environments'
        / 'local.py.template'
    )
    local_config = (
        PROJECT_DIRECTORY / 'server' / 'settings' / 'environments' / 'local.py'
    )
    shutil.copyfile(local_template, local_config)


copy_local_configuration()
print_futher_instuctions()
