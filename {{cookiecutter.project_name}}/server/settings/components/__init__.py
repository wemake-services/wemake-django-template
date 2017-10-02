# -*- coding: utf-8 -*-

import os

from fnmatch import fnmatch

from decouple import AutoConfig
from django.core.exceptions import ImproperlyConfigured
from unipath import Path


# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent.parent.parent.parent

# `unipath` is better than writing:
# BASE_DIR = dirname(dirname(dirname(dirname(__file__))))


class GlobalIPList(list):
    """
    Extra class to access development server from any IP inside the network
    """

    def __contains__(self, key):
        """
        This method works for IPs like: `192.168.0.*`
        """
        if any([fnmatch(key, elt) for elt in self]):
            return True
        return False


config = AutoConfig(search_path=os.path.join(BASE_DIR, 'config'))
