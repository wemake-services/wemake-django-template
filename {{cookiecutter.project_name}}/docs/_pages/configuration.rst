Configuration
=============

We share the same configuration structure for almost every possible environment.

We use:

- ``django-split-settings`` to organize ``django`` settings into multiple files and directories
- ``.env`` files to load secret configuration into different platforms


Components
----------

If you have some specific components like ``celery`` or ``mailgun`` installed, they could be configured in separate files. Just create a new file in ``server/settings/components/``. Then add it into ``server/settings/__init__.py``.


Environments
------------

To run ``django`` on different environments just specify ``DJANGO_ENV`` environment variable. It must have the same name as one of the files from ``server/settings/environments/``. Then values from this file will override other settings.


Local settings
--------------

If you need some specific local configuration tweaks, you can create file ``server/settings/environments/local.py.template`` to ``server/settings/environments/local.py``. It will be loaded into your settings automatically if exists.

.. code:: bash

  cp server/settings/environments/local.py.template server/settings/environments/local.py

See ``.template`` version for the reference.


Secret settings
---------------

We do not store our secret settings inside our source code.
There are different options to it:

- ``ansible-vault``
- ``git-secret``

Depending on a project we use both. But the main idea is that we place these settings into ``config/secret.env`` file. So it would be easily readable for both ``docker`` and ``django``.

You will need to copy file ``config/secret.env.template`` to ``config/secret.env``:

.. code:: bash

  cp config/secret.env.template config/secret.env


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


Utilities
---------

.. automodule:: server.settings.components

.. autoclass:: GlobalIPList
    :members:

.. autoclass:: DevelopmentConfiguration
    :members:
