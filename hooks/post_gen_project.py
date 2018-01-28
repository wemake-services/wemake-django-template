# -*- coding: utf-8 -*-

"""
Does the following:

1. Generates and saves random secret key
2. Removes docker files if it is not used

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
    https://github.com/django/django/blob/master/django/utils/crypto.py

And from pydanny's cookiecutter-django:
    https://github.com/pydanny/cookiecutter-django
"""

import os
import random
import shutil
import string

# CHANGEME mark
CHANGEME = '__CHANGEME__'

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False


def _get_random_string(length=50):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    punctuation = string.punctuation.replace('"', '').replace("'", '')
    punctuation = punctuation.replace('\\', '')
    if using_sysrandom:
        chars = string.digits + string.ascii_letters + punctuation
        return ''.join(random.choice(chars) for i in range(length))

    print(
        "Cookiecutter Django couldn't find a secure pseudo-random "
        'number generator on your system. '
        'Please change change your SECRET_KEY variables in config/.env '
        'manually.',
    )
    return CHANGEME


def _create_secret_key(config_path):
    with open(config_path) as f:
        file_ = f.read()

    # Generate a SECRET_KEY that matches the Django standard
    secret_key = _get_random_string()

    # Replace CHANGEME with SECRET_KEY
    file_ = file_.replace(CHANGEME, secret_key, 1)

    # Write the results to the file
    with open(config_path, 'w') as f:
        f.write(file_)


def copy_local_configuration():
    """
    Handler to copy local configuration from `.template`s
    to the actual files.
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
        PROJECT_DIRECTORY, 'server',
        'settings', 'environments', 'local.py.template',
    )
    local_config = os.path.join(
        PROJECT_DIRECTORY, 'server',
        'settings', 'environments', 'local.py',
    )
    shutil.copyfile(local_template, local_config)


def replace_pycharm_configuration():
    """
    Handler to replace CHANGEME marks inside `.idea` files.

    It is a workaround for a strange docker in PyCharm support.
    """
    files = [
        os.path.join(PROJECT_DIRECTORY, '.idea', 'misc.xml'),
        os.path.join(
            PROJECT_DIRECTORY, '.idea', '{{cookiecutter.project_name}}.iml',
        ),
    ]

    for name in files:
        with open(name) as f:
            file_ = f.read()

        # Replace CHANGEME with SECRET_KEY
        file_ = file_.replace(CHANGEME, PROJECT_DIRECTORY, 1)

        # Write the results to the file
        with open(name, 'w') as f:
            f.write(file_)


def clean_docker_files():
    """
    This function removes all docker-related files.
    It is called when user does not want to include docker support.
    """
    dockerignore = os.path.join(PROJECT_DIRECTORY, '.dockerignore')
    docker_compose = os.path.join(PROJECT_DIRECTORY, 'docker-compose.yml')
    docker_override = os.path.join(
        PROJECT_DIRECTORY, 'docker-compose.override.yml',
    )
    gitlab_ci = os.path.join(PROJECT_DIRECTORY, '.gitlab-ci.yml')
    docker_dir = os.path.join(PROJECT_DIRECTORY, 'docker')
    idea_dir = os.path.join(PROJECT_DIRECTORY, '.idea')

    docker_docs_root = os.path.join(
        PROJECT_DIRECTORY,
        'docs',
        '_pages',
        'template',
    )
    docker_related = (
        'docker.rst',
        'pycharm.rst',
        'gitlab-ci.rst',
        'going-to-production.rst',
        'production.rst',
    )

    for item in docker_related:
        os.remove(os.path.join(docker_docs_root, item))

    os.remove(dockerignore)
    os.remove(docker_compose)
    os.remove(docker_override)
    os.remove(gitlab_ci)
    shutil.rmtree(docker_dir)
    shutil.rmtree(idea_dir)


copy_local_configuration()

# Remove docker? {% if cookiecutter.docker != 'y' %}
clean_docker_files()  # {% else %}
replace_pycharm_configuration()
# {% endif %}
