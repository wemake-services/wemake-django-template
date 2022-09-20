# Logging
# https://docs.djangoproject.com/en/3.2/topics/logging/

# See also:
# 'Do not log' by Nikita Sobolev (@sobolevn)
# https://sobolevn.me/2020/03/do-not-log

from typing import TYPE_CHECKING, Callable

import structlog

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # We use these formatters in our `'handlers'` configuration.
    # Probably, you won't need to modify these lines.
    # Unless, you know what you are doing.
    'formatters': {
        'json_formatter': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.JSONRenderer(),
        },
        'console': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.KeyValueRenderer(
                key_order=['timestamp', 'level', 'event', 'logger'],
            ),
        },
    },

    # You can easily swap `key/value` (default) output and `json` ones.
    # Use `'json_console'` if you need `json` logs.
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'json_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json_formatter',
        },
    },

    # These loggers are required by our app:
    # - django is required when using `logger.getLogger('django')`
    # - security is required by `axes`
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'security': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}


class LoggingContextVarsMiddleware(object):
    """Used to reset ContextVars in structlog on each request."""

    def __init__(
        self,
        get_response: 'Callable[[HttpRequest], HttpResponse]',
    ) -> None:
        """Django's API-compatible constructor."""
        self.get_response = get_response

    def __call__(self, request: 'HttpRequest') -> 'HttpResponse':
        """
        Handle requests.

        Add your logging metadata here.
        Example: https://github.com/jrobichaud/django-structlog
        """
        response = self.get_response(request)
        structlog.contextvars.clear_contextvars()
        return response


if not structlog.is_configured():
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.filter_by_level,
            structlog.processors.TimeStamper(fmt='iso'),
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.ExceptionPrettyPrinter(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
