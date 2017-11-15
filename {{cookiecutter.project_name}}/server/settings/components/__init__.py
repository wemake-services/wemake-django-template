# -*- coding: utf-8 -*-

import os

from fnmatch import fnmatch

from decouple import AutoConfig
from unipath import Path


# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent.parent.parent.parent

# `unipath` is better than writing:
# BASE_DIR = dirname(dirname(dirname(dirname(__file__))))


class GlobalIPList(list):
    """
    Extra class to access development server from any IP inside the network.

    It uses globs to specify IP ranges.
    """

    def __contains__(self, key: str) -> bool:
        """
        Method to tests if IP is in subnet.

        It works for IPs like: `192.168.0.*`.
        """
        return any(fnmatch(key, elt) for elt in self)


config = AutoConfig(search_path=os.path.join(BASE_DIR, 'config'))
