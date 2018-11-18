.. _linters:

Linters
=======

This projects uses several linters to make coding style consistent.
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


xenon
-----

We are also using `xenon <https://github.com/rubik/xenon>`_ to measure
code complexity and quality.

Here are our standards:

- A single block of code can not go below ``A`` mark
- A single module can not go below ``A`` mark
- Overall mark can not go below ``A`` mark

If your commit breaks this rule: well, the build won't succeed.

.. code:: bash

  xenon --max-absolute A --max-modules A --max-average A server

It will return status code ``0`` if everything is fine.


yamllint
--------

Is used to lint your ``yaml`` files.
See `yamllint <https://github.com/adrienverge/yamllint>`_ docs.

.. code:: bash

  yamllint -d '{"extends": "default", "ignore": ".venv"}' -s .


Linters that are not included
-----------------------------

Sometimes we use several other linters that are not included.
That's because they require another technology stack to be installed
or just out of scope.

Here's the list of these linters. You may still find them useful.

shellcheck
~~~~~~~~~~

This linter is used to lint your ``.sh`` files.
See `shellcheck <https://www.shellcheck.net/>`_ docs.

hadolint
~~~~~~~~

This linter is used to lint your ``Dockerfile`` syntax.
See `hadolint <https://github.com/hadolint/hadolint>`_
