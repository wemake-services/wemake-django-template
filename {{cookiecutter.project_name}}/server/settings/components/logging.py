# Logging
# https://docs.djangoproject.com/en/1.11/topics/logging/

_VERBOSE = {
    'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
    'datefmt': '%d/%b/%Y %H:%M:%S',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': _VERBOSE,
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'server.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'server': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'security': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
