"""
This file contains a definition for Content-Security-Policy headers.

Read more about it:
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Content-Security-Policy

Docs: https://docs.djangoproject.com/en/stable/ref/csp/
"""

from django.utils.csp import CSP

# These values might and will be redefined in `development.py` env:
SECURE_CSP: dict[str, list[str | CSP]] = {
    'default-src': [CSP.NONE],
    'script-src': [CSP.SELF],
    'style-src': [CSP.SELF],
    'img-src': [CSP.SELF],
    'font-src': [CSP.SELF],
    'connect-src': [],
}
