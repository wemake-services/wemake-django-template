Security
========

Security is our first priority.
We try to make projects as secure as possible.
We use a lot of 3rd party tools to achieve that.


Django
------

Django has a lot of `security-specific settings <https://docs.djangoproject.com/en/1.11/topics/security/>`_
that are all turned on by default.

We also enforce ``https`` only access in production.

We also use a set of custom ``django`` apps to enforce even more security:

- `django-axes <https://github.com/jazzband/django-axes>`_ to track and ban repeating access requests
- `django-csp <https://github.com/mozilla/django-csp>`_ to enforce `Content-Security Policy <https://www.w3.org/TR/CSP/>`_ for our webpages
- `django-referrer-policy <https://django-referrer-policy.readthedocs.io>`_ to enforce `Referrer Policy <https://www.w3.org/TR/referrer-policy/>`_ for our webpages

And there are also some awesome extensions that are not included:

- `django-honeypot <https://github.com/jamesturk/django-honeypot>`_ - django application that provides utilities for preventing automated form spam


Dependencies
------------

We use `poetry <https://poetry.eustace.io/>`_ which ensures
that all the dependencies hashes match during the installation process.
Otherwise, the build will fail. So, it is almost impossible to

We also use `safety <https://github.com/pyupio/safety>`_
to analyze vulnerable dependencies to prevent the build
to go to the production with unsafe dependencies.


Static analysis
---------------

We use ``wemake-python-styleguide`` which
includes `bandit <https://pypi.org/project/bandit/>`_ security checks inside.

You can also install `pyt <https://pyt.readthedocs.io>`_
which is not included by default.
It will include even more static checks for ``sql`` injections, ``xss`` and others.


Audits
------

The only way to be sure that your app is secure is to audit it in production.
The are different tools to help you:

- `twa <https://github.com/trailofbits/twa>`_ - tiny web auditor that has a lot of security checks
- `XSStrike <https://github.com/s0md3v/XSStrike>`_ - automated tool to check that your application is not vulnerable to ``xss`` errors
