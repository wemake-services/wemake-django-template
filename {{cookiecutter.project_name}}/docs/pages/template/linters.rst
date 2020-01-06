.. _linters:

Linters
=======

This project uses several linters to make coding style consistent.
All configuration is stored inside ``setup.cfg``.


wemake-python-styleguide
------------------------

``wemake-python-styleguide`` is a ``flake8`` based plugin.
And it is also the strictest and most opinionated python linter ever.
See `wemake-python-styleguide <https://wemake-python-styleguide.readthedocs.io/en/latest/>`_
docs.

Things that are included in the linting process:

- `flake8 <http://flake8.pycqa.org/>`_ is used a general tool for linting
- `isort <https://github.com/timothycrosley/isort>`_ is used to validate ``import`` order
- `bandit <https://github.com/PyCQA/bandit>`_ for static security checks
- `eradicate <https://github.com/myint/eradicate>`_ to find dead code
- and more!

Running linting process for all ``python`` files in the project:

.. code:: bash

  flake8 .

Extra plugins
~~~~~~~~~~~~~

We also use some extra plugins for ``flake8``
that are not bundled with ``wemake-python-styleguide``:

- `flake8-pytest <https://github.com/vikingco/flake8-pytest>`_ - ensures that ``pytest`` best practices are used
- `flake8-pytest-style <https://github.com/m-burst/flake8-pytest-style>`_ - ensures that ``pytest`` tests and fixtures are written in a single style
- `flake8-django <https://github.com/rocioar/flake8-django>`_ - plugin to enforce best practices in a ``django`` project


django-migration-linter
-----------------------

We use ``django-migration-linter`` to find backward incompatible migrations.
It allows us to write 0-downtime friendly code.

See `django-migration-linter <https://github.com/3YOURMIND/django-migration-linter>`_
docs, it contains a lot of useful information about ways and tools to do it.

That's how this check is executed:

.. code:: bash

  python manage.py lintmigrations --exclude-apps=axes

Important note: you might want to exclude some packages with broken migrations.
Sometimes, there's nothing we can do about it.


yamllint
--------

Is used to lint your ``yaml`` files.
See `yamllint <https://github.com/adrienverge/yamllint>`_ docs.

.. code:: bash

  yamllint -d '{"extends": "default", "ignore": ".venv"}' -s .


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

We also use ``pip`` and ``poetry`` self checks to be sure
that packaging works correctly.

.. code:: bash

  poetry check && pip check


Linters that are not included
-----------------------------

Sometimes we use several other linters that are not included.
That's because they require another technology stack to be installed
or just out of scope.

We also recommend to check the list of linters
`recommended by wemake-python-styleguide <https://wemake-python-stylegui.de/en/latest/pages/usage/integrations/extras.html>`_.

Here's the list of these linters. You may still find them useful.

shellcheck
~~~~~~~~~~

This linter is used to lint your ``.sh`` files.
See `shellcheck <https://www.shellcheck.net/>`_ docs.

hadolint
~~~~~~~~

This linter is used to lint your ``Dockerfile`` syntax.
See `hadolint <https://github.com/hadolint/hadolint>`_
