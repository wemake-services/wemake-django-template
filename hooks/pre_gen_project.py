# -*- coding: utf-8 -*-

import re
import sys

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


MODULE_REGEX = r'^[a-z][_a-z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_name }}'

DOMAIN_NAME = '{{ cookiecutter.project_url }}'

if not re.match(MODULE_REGEX, MODULE_NAME):
    # Validates project's module name:
    message = (
        'ERROR: The project slug {} is not a valid Python module name.'
        'Please do not use a - and use _ instead'
    )
    print(message.format(MODULE_NAME))

    sys.exit(1)  # exit to cancel project.

try:
    # Validates project's domain:
    result = urlparse(DOMAIN_NAME)
    parts = [result.path]
    if not all(bool(part) for part in parts):
        raise ValueError('Mailformed project_url')
except Exception as e:
    print(e)

    sys.exit(1)
