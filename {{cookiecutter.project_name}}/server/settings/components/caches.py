# -*- coding: utf-8 -*-

# Caching
# https://docs.djangoproject.com/en/1.11/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'axes_cache': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}


# django-axes
# https://django-axes.readthedocs.io/en/latest/configuration.html
# See #known-configuration-problems section

AXES_CACHE = 'axes_cache'
