.. _django:

Django
======


Configuration
-------------

We share the same configuration structure for almost every possible
environment.

We use:

- ``django-split-settings`` to organize ``django``
  settings into multiple files and directories
- ``.env`` files to store secret configuration
- ``python-decouple`` to load ``.env`` files into ``django``

Components
~~~~~~~~~~

If you have some specific components like ``celery`` or ``mailgun`` installed,
they could be configured in separate files.
Just create a new file in ``server/settings/components/``.
Then add it into ``server/settings/__init__.py``.

Environments
~~~~~~~~~~~~

To run ``django`` on different environments just
specify ``DJANGO_ENV`` environment variable.
It must have the same name as one of the files
from ``server/settings/environments/``.
Then, values from this file will override other settings.

Local settings
~~~~~~~~~~~~~~

If you need some specific local configuration tweaks,
you can create file ``server/settings/environments/local.py.template``
to ``server/settings/environments/local.py``.
It will be loaded into your settings automatically if exists.

.. code:: bash

  cp server/settings/environments/local.py.template server/settings/environments/local.py

See ``local.py.template`` version for the reference.


Secret settings
---------------

We share the same mechanism for secret settings for all our tools.
We use ``.env`` files for ``django``, ``postgres``, ``docker``, etc.

Initially, you will need to copy file
``config/.env.template`` to ``config/.env``:

.. code:: bash

  cp config/.env.template config/.env

When adding any new secret ``django`` settings you will need to:

1. Add new key and value to ``config/.env``
2. Add new key without value to ``config/.env.template``,
   add a comment on how to get this value for other users
3. Add new variable inside ``django`` settings
4. Use ``python-decouple`` to load this ``env`` variable like so:
   ``MY_SECRET = config('MY_SECRET')``


Secret settings in production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We do not store our secret settings inside our source code.
All sensible settings are stored in ``config/.env`` file,
which is not tracked by the version control.

So, how do we store secrets? We store them as secret environment variables
in `GitLab CI <https://docs.gitlab.com/ce/ci/variables/README.html#secret-variables>`_.
Then we use `dump-env <https://github.com/sobolevn/dump-env>`_
to dump variables from both environment and ``.env`` file template.
Then, this file is copied inside ``docker`` image and when
this image is built - everything is ready for production.

Here's an example:

1. We add a ``SECRET_DJANGO_SECRET_KEY`` variable to Gitlab CI secret variables
2. Then ``dump-env`` dumps ``SECRET_DJANGO_SECRET_KEY``
   as ``DJANGO_SECRET_KEY`` and writes it to ``config/.env`` file
3. Then it is loaded by ``django`` inside the settings:
   ``SECRET_KEY = config('DJANGO_SECRET_KEY')``

However, there are different options to store secret settings:

- `ansible-vault <https://docs.ansible.com/ansible/2.4/vault.html>`_
- `git-secret <https://github.com/sobolevn/git-secret>`_
- `Vault <https://www.vaultproject.io/>`_

Depending on a project we use different tools.
With ``dump-env`` being the default and the simplest one.


Extensions
----------

We use different ``django`` extensions that make your life easier.
Here's a full list of the extensions for both development and production:

- `django-split-settings`_ - organize
  ``django`` settings into multiple files and directories.
  Easily override and modify settings.
  Use wildcards in settings file paths and mark settings files as optional
- `django-axes`_ - keep track
  of failed login attempts in ``django`` powered sites
- `django-csp`_ - `Content Security Policy`_ for ``django``
- `django-referrer-policy`_ - middleware implementing the `Referrer-Policy`_
- `django-health-check`_ - checks for various conditions and provides reports
  when anomalous behavior is detected
- `django-add-default-value`_ - this django Migration Operation can be used to
  transfer a Fields default value to the database scheme
- `django-deprecate-fields`_ - this package allows deprecating model fields and
  allows removing them in a backwards compatible manner
- `django-migration-linter`_ - detect backward incompatible migrations for
  your django project
- `zero-downtime-migrations`_ - apply ``django`` migrations on PostgreSql
  without long locks on tables

Development only extensions:

- `django-debug-toolbar`_ - a configurable set of panels that
  display various debug information about the current request/response
- `django-querycount`_ - middleware that prints the number
  of DB queries to the runserver console
- `nplusone`_ - auto-detecting the `n+1 queries problem`_ in ``django``

.. _django-split-settings: https://github.com/sobolevn/django-split-settings
.. _django-axes: https://github.com/jazzband/django-axes
.. _django-csp: https://github.com/mozilla/django-csp
.. _`Content Security Policy`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy
.. _django-referrer-policy: https://github.com/ubernostrum/django-referrer-policy
.. _`Referrer-Policy`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
.. _django-health-check: https://github.com/KristianOellegaard/django-health-check
.. _django-add-default-value: https://github.com/3YOURMIND/django-add-default-value
.. _django-deprecate-fields: https://github.com/3YOURMIND/django-deprecate-fields
.. _django-migration-linter: https://github.com/3YOURMIND/django-migration-linter
.. _zero-downtime-migrations: https://github.com/yandex/zero-downtime-migrations
.. _django-debug-toolbar: https://github.com/jazzband/django-debug-toolbar
.. _django-querycount: https://github.com/bradmontgomery/django-querycount
.. _nplusone: https://github.com/jmcarp/nplusone
.. _`n+1 queries problem`: https://stackoverflow.com/questions/97197/what-is-the-n1-select-query-issue


Further reading
---------------

- `django-split-settings tutorial <https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d>`_
- `docker env-file docs <https://docs.docker.com/compose/env-file/>`_


Django admin
~~~~~~~~~~~~

- `Django Admin Cookbook <https://books.agiliq.com/projects/django-admin-cookbook/en/latest/>`_
