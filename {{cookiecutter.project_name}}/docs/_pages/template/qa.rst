.. _qa:

QA
==

We try to keep our quality standards high.
So, we use different tools to make this possible.

First of all, we use `mypy <http://mypy-lang.org/>`_ for optional
static typing.

We are also using `radon <https://github.com/rubik/radon>`_ and
`xenon <https://github.com/rubik/xenon>`_ to measure
code complexity and quality.

We use `bandit <https://github.com/PyCQA/bandit>`_ for static security checks.


radon
-----

Rules
~~~~~

Here are our standards:

- A single block of code can not go below ``B`` mark
- A single module can not go below ``A`` mark
- Overall mark can not go below ``A`` mark

If your commit breaks this rule: well, the build won't succeed.

Running code analysis
~~~~~~~~~~~~~~~~~~~~~

There are several metrics we use.

Cyclomatic Comlexity:

.. code:: bash

  radon cc . -a

Maintainability Index:

.. code:: bash

  radon mi .

And at last but not least, raw metrics:

.. code:: bash

  radon raw .

Running validation
~~~~~~~~~~~~~~~~~~

If you would like to run QA by hand:

.. code:: bash

  xenon --max-absolute B --max-modules A --max-average A .

It will return status code ``0`` if everything is fine.


mypy
----

Running ``mypy`` is required before any commit:

.. code:: bash

    mypy server

This will eliminate a lot of possible ``TypeError`` and other issues.
However, this will not make code 100% working.
So, testing and reviewing is still required.

``mypy`` is configured via ``setup.cfg``.
Read the `docs <https://mypy.readthedocs.io/en/latest/>`_
for more information.


bandit
------

Running ``bandit`` is required before any commit:

.. code:: bash

    bandit -r server

This will find possible XSS errors, insecure operations, and other issues.
Read the `docs for bandit <https://bandit.readthedocs.io>`_.
