.. _configuration:

Configuration
=============

We share the same configuration structure for almost every possible
environment.

We use:

- ``django-split-settings`` to organize ``django``
  settings into multiple files and directories
- ``.env`` files to load secret configuration into different platforms


Components
----------

If you have some specific components like ``celery`` or ``mailgun`` installed,
they could be configured in separate files.
Just create a new file in ``server/settings/components/``.
Then add it into ``server/settings/__init__.py``.


Environments
------------

To run ``django`` on different environments just
specify ``DJANGO_ENV`` environment variable.
It must have the same name as one of the files
from ``server/settings/environments/``.
Then values from this file will override other settings.


Local settings
--------------

If you need some specific local configuration tweaks,
you can create file ``server/settings/environments/local.py.template``
to ``server/settings/environments/local.py``.
It will be loaded into your settings automatically if exists.

.. code:: bash

  cp server/settings/environments/local.py.template server/settings/environments/local.py

See ``.template`` version for the reference.


Secret settings
---------------

You will need to copy file ``config/.env.template`` to ``config/.env``:

.. code:: bash

  cp config/.env.template config/.env


Secret settings in production
-----------------------------

We do not store our secret settings inside our source code.
All sensible settings are stored in ``config/.env`` file,
which is not tracked by the version control.

So, how do we store secrets? We store them as secret environment variables
in `GitLab CI <https://docs.gitlab.com/ce/ci/variables/README.html#secret-variables>`_.
Then we use `dump-env <https://github.com/sobolevn/dump-env>`_
to dump variables from both environment and ``.env`` file template.
Then, this file is copied inside ``docker`` image and when
this image is built - everything is ready for production.

Example store secret variables with dump-env and Gitlab CI:

1. We add a ``SECRET_DJANGO_SECRET_KEY`` variable to Gitlab CI Secret Variables;
2. Before build in CI ``dump-env`` dump ``SECRET_DJANGO_SECRET_KEY``
   as ``DJANGO_SECRET_KEY``
3. ``dump-env`` save ``DJANGO_SECRET_KEY`` to ``.env`` file.
4. Now Django use this value in settings.

However, there are different options to store secret settings:

- `ansible-vault <https://docs.ansible.com/ansible/2.4/vault.html>`_
- `git-secret <https://github.com/sobolevn/git-secret>`_
- `Vault <https://www.vaultproject.io/>`_

Depending on a project we use different tools.
With ``dump-env`` being the default and the simplest one.

But the main idea is that we place these settings into ``config/.env`` file.
So it would be easily readable for both ``docker`` and ``django``.


Further reading
---------------

- ``django-split-settings`` `tutorial`_
- ``django-split-settings`` `docs`_
- ``git-secret`` `site`_
- ``docker`` `env-file docs`_

.. _tutorial: https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d
.. _docs: http://django-split-settings.readthedocs.io/en/latest/
.. _site: http://git-secret.io/
.. _`env-file docs`: https://docs.docker.com/compose/env-file/
