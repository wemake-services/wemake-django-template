"""
This file contains a definition for Content-Security-Policy headers.

Read more about it:
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Content-Security-Policy

We are using `django-csp` to provide these headers.
Docs: https://github.com/mozilla/django-csp
"""

from typing import TypedDict, final

from csp.constants import NONE, SELF


@final
class _ContentSecurityPolicy(TypedDict):
    EXCLUDE_URL_PREFIXES: list[str]  # noqa: WPS115
    DIRECTIVES: dict[str, list[str]]  # noqa: WPS115


# These values might and will be redefined in `development.py` env:
CONTENT_SECURITY_POLICY: _ContentSecurityPolicy = {
    'EXCLUDE_URL_PREFIXES': [
        '/docs/stoplight/',
        '/docs/swagger/',
        '/docs/scalar/',
        '/docs/redoc/',
    ],
    'DIRECTIVES': {
        'default-src': [NONE],
        'script-src': [SELF],
        'style-src': [SELF],
        'img-src': [SELF],
        'font-src': [SELF],
        'connect-src': [],
    },
}
