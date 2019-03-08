# -*- coding: utf-8 -*-

"""
This file contains a definition for Content-Security-Policy headers.

Read more about it:
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Content-Security-Policy

We are using `django-csp` to provide these headers.
Docs: https://github.com/mozilla/django-csp
"""

CSP_SCRIPT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
CSP_DEFAULT_SRC = ("'none'",)
