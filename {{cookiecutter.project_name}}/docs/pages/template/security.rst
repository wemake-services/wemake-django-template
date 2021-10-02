Security
========

Security is our first priority.
We try to make projects as secure as possible.
We use a lot of 3rd party tools to achieve that.


Django
------

Django has a lot of `security-specific settings <https://docs.djangoproject.com/en/3.2/topics/security/>`_
that are all turned on by default in this template.

We also :ref:`enforce <going-to-production>` all the best practices
by running ``django`` checks inside CI for each commit.

We also use a set of custom ``django`` apps
to enforce even more security rules:

- `django-axes <https://github.com/jazzband/django-axes>`_ to track and ban repeating access requests
- `django-csp <https://github.com/mozilla/django-csp>`_ to enforce `Content-Security Policy <https://www.w3.org/TR/CSP/>`_ for our webpages
- `django-http-referrer-policy <https://django-referrer-policy.readthedocs.io>`_ to enforce `Referrer Policy <https://www.w3.org/TR/referrer-policy/>`_ for our webpages

And there are also some awesome extensions that are not included:

- `django-honeypot <https://github.com/jamesturk/django-honeypot>`_ - django application that provides utilities for preventing automated form spam

Passwords
~~~~~~~~~

We use strong algorithms for password hashing:
``bcrypt``, ``PBKDF2`` and ``Argon2`` which are known to be secure enough.


Dependencies
------------

We use `poetry <https://poetry.eustace.io/>`_ which ensures
that all the dependencies hashes match during the installation process.
Otherwise, the build will fail.
So, it is almost impossible to replace an already existing package
with a malicious one.

We also use `safety <https://github.com/pyupio/safety>`_
to analyze vulnerable dependencies to prevent the build
to go to the production with known unsafe dependencies.

.. code:: bash

  safety check

We also use `Github security alerts <https://help.github.com/articles/about-security-alerts-for-vulnerable-dependencies/>`_
for our main template repository.


Static analysis
---------------

We use ``wemake-python-styleguide`` which
includes `bandit <https://pypi.org/project/bandit/>`_ security checks inside.

You can also install `pyt <https://pyt.readthedocs.io>`_
which is not included by default.
It will include even more static checks for
``sql`` injections, ``xss`` and others.


Dynamic analysis
----------------

You can monitor your running application to detect anomalous activities.
Tools to consider:

- `dagda <https://github.com/eliasgranderubio/dagda>`_ - a tool to perform static analysis of known vulnerabilities, trojans, viruses, malware & other malicious threats in docker images/containers and to monitor the docker daemon and running docker containers for detecting anomalous activities

All the tools above are not included into this template.
You have to install them by yourself.


Secrets
-------

We store secrets separately from code. So, it is harder for them to leak.
However, we encourage to use tools like
`truffleHog <https://github.com/dxa4481/truffleHog>`_ or `detect-secrets <https://github.com/Yelp/detect-secrets>`_ inside your workflow.

You can also turn on `Gitlab secrets checker <https://docs.gitlab.com/ee/push_rules/push_rules.html#prevent-pushing-secrets-to-the-repository>`_ which we highly recommend.


Audits
------

The only way to be sure that your app is secure
is to constantly audit it in production.

There are different tools to help you:

- `twa <https://github.com/trailofbits/twa>`_ - tiny web auditor that has a lot of security checks for the webpages
- `XSStrike <https://github.com/s0md3v/XSStrike>`_ - automated tool to check that your application is not vulnerable to ``xss`` errors
- `docker-bench <https://github.com/docker/docker-bench-security>`_ - a script that checks for dozens of common best-practices around deploying Docker containers in production
- `lynis <https://cisofy.com/lynis/>`_ - a battle-tested security tool for systems running Linux, macOS, or Unix-based operating system
- `trivy <https://github.com/knqyf263/trivy>`_ - a simple and comprehensive vulnerability scanner for containers

But, even after all you attempts to secure your application,
it **won't be 100% safe**. Do not fall into this false feeling of security.


Further reading
---------------

- `Open Web Application Security Project <https://www.owasp.org/images/3/33/OWASP_Application_Security_Verification_Standard_3.0.1.pdf>`_
- `Docker security <https://docs.docker.com/engine/security/security/>`_
- `AppArmor <https://docs.docker.com/engine/security/apparmor/>`_ and `bane <https://github.com/genuinetools/bane>`_
