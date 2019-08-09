#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def main():
    """
    Main function.

    It does several things:
    1. Sets default settings module, if it is not set
    2. Warns if Django is not installed
    3. Executes any given command
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

    try:
        from django.core import management  # noqa: WPS433
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:  # noqa: WPS505
            import django  # noqa: WPS433, F401
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and " +
                'available on your PYTHONPATH environment variable? Did you ' +
                'forget to activate a virtual environment?',
            )
        raise

    management.execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
