.. _linters:

Linters
=======

This project uses several linters to make coding style consistent.
All configuration is stored inside ``setup.cfg`` and ``pyproject.toml``.


ruff
----

We use ``ruff`` to format and lint our code.

To run:

.. code:: bash

  ruff check && ruff format

See `ruff docs <https://docs.astral.sh/ruff>`_ on how to use it.
The configuration is stored in ``pyproject.toml``.


wemake-python-styleguide
------------------------

``wemake-python-styleguide`` is a ``flake8`` based plugin.
And it is also the strictest and most opinionated python linter ever.
See `wemake-python-styleguide <https://wemake-python-styleguide.readthedocs.io/en/latest/>`_
docs.

Running linting process for all ``python`` files in the project:

.. code:: bash

  flake8 .


django-migration-linter
-----------------------

We use ``django-migration-linter`` to find backward incompatible migrations.
It allows us to write 0-downtime friendly code.

See `django-migration-linter <https://github.com/3YOURMIND/django-migration-linter>`_
docs, it contains a lot of useful information about ways and tools to do it.

That's how this check is executed:

.. code:: bash

  python manage.py lintmigrations

Important note: you might want to exclude some packages with broken migrations.
Sometimes, there's nothing we can do about it.


django-safe-migrations
----------------------

We use ``django-safe-migrations`` to ensure our database migrations are safe
to run in production environments without downtime. It provides checks and
utilities to prevent unsafe operations such as locking tables or breaking
existing queries.

See `django-safe-migrations <https://github.com/YasserShkeir/django-safe-migrations>`_
docs, it contains useful information and best practices for writing safe migrations.

That's how this check is executed:

.. code:: bash

  python manage.py check_migrations --exclude-apps=axes

Important note: some third-party apps may include migrations that are not fully safe.
In such cases, consider reviewing them manually or excluding them from checks
if no fix is possible.


yamllint
--------

Is used to lint your ``yaml`` files.
See `yamllint <https://github.com/adrienverge/yamllint>`_ docs.

.. code:: bash

  yamllint -d '{"extends": "default", "ignore": ".venv"}' -s .


djangofmt
---------

Is used to lint and format your ``html`` files.
See `djangofmt <https://github.com/UnknownPlatypus/djangofmt>`_ docs.

.. code:: bash

  find server -type f -name '*.html' | xargs djangofmt \
    --line-length=80 --indent-width=2


import-linter
-------------

Is used to lint your architecture and imports all across the project.
See `import-linter <https://github.com/seddonym/import-linter>`_ docs.

.. code:: bash

  lint-imports


dotenv-linter
-------------

Is used to lint your ``.env`` files.
See `dotenv-linter <https://github.com/wemake-services/dotenv-linter>`_ docs.

.. code:: bash

  dotenv-linter config/.env config/.env.template


polint and dennis
-----------------

Are used to lint your ``.po`` files.
See `polint <https://github.com/ziima/polint>`_ docs.
Also see `dennis <https://dennis.readthedocs.io/en/latest/linting.html>`_ docs.

.. code:: bash

  polint -i location,unsorted locale
  dennis-cmd lint --errorsonly locale


Packaging
---------

We also use ``uv`` and ``pip`` self checks to be sure
that packaging works correctly.

.. code:: bash

  uv lock --check && pip check


Linters that are not included
-----------------------------

Sometimes we use several other linters that are not included.
That's because they require another technology stack to be installed
or just out of scope.

shellcheck
~~~~~~~~~~

This linter is used to lint your ``.sh`` files.
See `shellcheck <https://www.shellcheck.net/>`_ docs.

hadolint
~~~~~~~~

This linter is used to lint your ``Dockerfile`` syntax.
See `hadolint <https://github.com/hadolint/hadolint>`_
