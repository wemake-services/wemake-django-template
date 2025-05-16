"""
Gunicorn configuration file
https://docs.gunicorn.org/en/stable/configure.html#configuration-file
https://docs.gunicorn.org/en/stable/settings.html

Gunicorn configuration file for running in synchronous mode.
The setup requires an environment variable `GUNICORN_WSGI_SETTINGS`,
which contains the launch parameters for the Gunicorn process/workers.

The `GUNICORN_WSGI_SETTINGS` environment variable should contain a string with a Python dictionary inside,
specifying the Gunicorn launch parameters.

Example of the environment variable:

```
GUNICORN_WSGI_SETTINGS = '{"wsgi_app": "config.wsgi:application", "workers": 4, "bind": "0.0.0.0:8000", "accesslog": "-"}'
```

The available configuration parameters are listed https://docs.gunicorn.org/en/22.0.0/settings.html.
When adding a new parameter, its default value should be included in the `GUNICORN_DEFAULTS` dictionary,
and the value from the environment variable should be assigned in this file.

For more details on available Gunicorn configuration parameters, see: https://docs.gunicorn.org/en/22.0.0/settings.html
"""

import os
from ast import literal_eval
from types import MappingProxyType
from typing import Any, override


class GunicornConfigError(Exception):
    """
    Raised when the Gunicorn configuration environment variable is invalid.
    A valid variable should be a string containing a dictionary of the configuration.

    Example env: '{"wsgi_app": "config.wsgi:application", "workers": 8, "bind": "0.0.0.0:8000", "accesslog": "-"}'
    """

    def __init__(self, message: str, env_name: str) -> None:
        self.message = message
        self.env_name = env_name
        super().__init__(self.message)

    @override
    def __str__(self) -> str:
        current_env_value = os.getenv(self.env_name, 'Not set')
        return (
            f'GunicornConfigError: {self.message}\n'
            f'Environment variable: {self.env_name}\n'
            f'Current value: {current_env_value}\n'
        )


GUNICORN_WSGI_SETTINGS = {}
if env_value := os.getenv('GUNICORN_WSGI_SETTINGS', ''):
    try:
        GUNICORN_WSGI_SETTINGS = literal_eval(env_value)
    except (ValueError, SyntaxError) as e:
        raise GunicornConfigError(
            'Error loading WSGI gunicorn config from environment variables',
            'GUNICORN_WSGI_SETTINGS',
        ) from None


GUNICORN_WSGI_DEFAULTS: MappingProxyType[str, Any] = MappingProxyType({
    'accesslog': '-',
    'access_log_format': '%({X-Real-IP}i)s %(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s %(L)s %(p)s',
    'errorlog': '-',
    'loglevel': 'info',
    'preload_app': False,
    'wsgi_app': 'config.wsgi:application',
    'workers': 1,
    'worker_class': 'sync',
    'threads': 1,
    'worker_connections': 1000,
    'max_requests': 0,
    'max_requests_jitter': 0,
    'timeout': 120,
    'graceful_timeout': 30,
    'keepalive': 2,
    'bind': '0.0.0.0:8000',
    'chdir': '/code',
    'worker_tmp_dir': '/dev/shm',
})

# https://docs.gunicorn.org/en/22.0.0/settings.html#wsgi-app
wsgi_app = GUNICORN_WSGI_SETTINGS.get(
    'wsgi_app', GUNICORN_WSGI_DEFAULTS['wsgi_app']
)

# https://docs.gunicorn.org/en/22.0.0/settings.html#bind
bind = GUNICORN_WSGI_SETTINGS.get('bind', GUNICORN_WSGI_DEFAULTS['bind'])

# https://docs.gunicorn.org/en/22.0.0/settings.html#worker-processes
workers = GUNICORN_WSGI_SETTINGS['workers']
worker_class = GUNICORN_WSGI_SETTINGS.get(
    'worker_class', GUNICORN_WSGI_DEFAULTS['worker_class']
)
threads = GUNICORN_WSGI_SETTINGS.get(
    'threads', GUNICORN_WSGI_DEFAULTS['threads']
)
worker_connections = GUNICORN_WSGI_SETTINGS.get(
    'worker_connections', GUNICORN_WSGI_DEFAULTS['worker_connections']
)
max_requests = GUNICORN_WSGI_SETTINGS.get(
    'max_requests', GUNICORN_WSGI_DEFAULTS['max_requests']
)
max_requests_jitter = GUNICORN_WSGI_SETTINGS.get(
    'max_requests_jitter', GUNICORN_WSGI_DEFAULTS['max_requests_jitter']
)
timeout = GUNICORN_WSGI_SETTINGS.get(
    'timeout', GUNICORN_WSGI_DEFAULTS['timeout']
)
graceful_timeout = GUNICORN_WSGI_SETTINGS.get(
    'graceful_timeout', GUNICORN_WSGI_DEFAULTS['graceful_timeout']
)
keepalive = GUNICORN_WSGI_SETTINGS.get(
    'keepalive', GUNICORN_WSGI_DEFAULTS['keepalive']
)

# https://docs.gunicorn.org/en/22.0.0/settings.html#logging
accesslog = GUNICORN_WSGI_SETTINGS.get(
    'accesslog', GUNICORN_WSGI_DEFAULTS['accesslog']
)
access_log_format = GUNICORN_WSGI_SETTINGS.get(
    'access_log_format', GUNICORN_WSGI_DEFAULTS['access_log_format']
)
errorlog = GUNICORN_WSGI_SETTINGS.get(
    'errorlog', GUNICORN_WSGI_DEFAULTS['errorlog']
)
loglevel = GUNICORN_WSGI_SETTINGS.get(
    'loglevel', GUNICORN_WSGI_DEFAULTS['loglevel']
)

# https://docs.gunicorn.org/en/22.0.0/settings.html#server-mechanics
preload_app = GUNICORN_WSGI_SETTINGS.get(
    'preload_app', GUNICORN_WSGI_DEFAULTS['preload_app']
)
chdir = GUNICORN_WSGI_SETTINGS.get('chdir', GUNICORN_WSGI_DEFAULTS['chdir'])
worker_tmp_dir = GUNICORN_WSGI_SETTINGS.get(
    'worker_tmp_dir', GUNICORN_WSGI_DEFAULTS['worker_tmp_dir']
)
