# Logging
# https://docs.djangoproject.com/en/1.11/topics/logging/
# and
# http://www.structlog.org/en/stable/standard-library.html

import structlog

timestamper = structlog.processors.TimeStamper(fmt='%Y-%m-%d %H:%M:%S')
pre_chain = [
    # Add the log level and a timestamp to the event_dict if the log entry
    # is not from structlog.
    structlog.stdlib.add_log_level,
    timestamper,
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'plain': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.dev.ConsoleRenderer(colors=False),
            'foreign_pre_chain': pre_chain,
        },
        'colored': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.dev.ConsoleRenderer(colors=True),
            'foreign_pre_chain': pre_chain,
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'server.log',
            'formatter': 'plain',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
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
        '': {
            'handlers': ['default', 'file'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        timestamper,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
