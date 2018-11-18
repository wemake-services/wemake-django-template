Dependencies
============

We use ``poetry`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.
Before going any further, please,
take a moment to read the `official documentation <https://poetry.eustace.io/>`_
about ``poetry`` to know some basics.


Installing all dependencies
---------------------------

Please, note that ``poetry`` will automatically create a ``virtualenv`` for
this project. It will use you current ``python`` version.
To install all existing dependencies run:

.. code:: bash

  poetry install


Installing dependencies for production use
------------------------------------------

To install dependencies for production use, you will need to run:

.. code:: bash

  poetry install --no-dev


Activating virtualenv
---------------------

And to activate ``virtualenv`` created by ``poetry`` run:

.. code:: bash

  poetry shell


Adding new dependencies
-----------------------

To add a new dependency you can run:

- ``poetry add django`` to install ``django`` as a production dependency
- ``poetry add --dev pytest`` to install ``pytest``
  as a development dependency


Dependencies security
---------------------

We use ``safety`` to validate that we use only secure releases.
To validate that all dependencies are secure, run:

.. code:: bash

   safety check


Updating poetry version
-----------------------

Package managers should also be pinned very strictly.
We had a lot of problems in production
because we were not pinning package manager versions.

This can result in broken ``lock`` files, inconsistent installation process,
bizarre bugs, and missing packages. You do not want to experience that!

How can we have the same ``poetry`` version for all users in a project?
That's where ``[build-system]`` tag shines. It specifies the exact version of
your ``poetry`` installation that must be used for the project.
Version mismatch will fail your build.

When you to update ``poetry``, you have to bump it in several places:

1. ``pyproject.toml``
2. ``docker/django/Dockerfile``

Then you are fine!
