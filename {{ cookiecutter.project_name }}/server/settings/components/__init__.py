# -*- coding: utf-8 -*-

""" Defining basic logic for the app."""

import os

from os.path import join, isfile, dirname
from fnmatch import fnmatch

import toml

from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(dirname(__file__))))


class GlobalIPList(list):
    """
    Extra class to access development server from any IP inside the network
    """

    def __contains__(self, key):
        if any([fnmatch(key, elt) for elt in self]):
            return True
        return False


class DevelopmentConfiguration(object):
    """
    This class reads the text file formatted as `toml`

    This class is used to speed up the development process.
    """

    def __init__(self, *path_parts):
        """
        Reads the file and prepares config.

        :param path_parts: Path to the configuration file,
            ensure that this file is excluded from VCS.
        """
        self.path = join(*path_parts)
        self._config = toml.load(self.path)

    def __getitem__(self, item):
        """
        This function is used to get a specific settings' value.

        :param item: Key to get the needed value.
        :return: Value from secret file if present. Empty string otherwise.
        """
        return self._config.get(item, '')


CONFIG = DevelopmentConfiguration(BASE_DIR, 'config', 'secret.toml')
