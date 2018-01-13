.. _qa:

QA
==

We try to keep our quality standards high. So, we use different tools to make this possible.

First of all, we use `mypy <http://mypy-lang.org/>`_ for optional static typing.

We are also using `radon <https://github.com/rubik/radon>`_ and `xenon <https://github.com/rubik/xenon>`_ to measure code complexity and quality.


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

    python -m mypy server

This will eliminate a lot of possible ``TypeError``s and other issues.
However, this will not make code 100% working. So, testing and reviewing is still required.

``mypy`` is configured via ``setup.cfg``. Read the `docs <https://mypy.readthedocs.io/en/latest/>`_ for more information.


vulture
-------

We use ``vulture`` to reduce possible dead code.
However, it is not a required step in our CI process.
Since sometimes ``python`` code can be tricky, and absolutely valid code is considered unused.

We only collect usage stats as an artifact and sometimes check this metric while developing.

Running ``vulture`` is simple:

.. code:: bash

    vulture server tests --exclude server/settings/

Note, that ``server/settings`` is excluded, because it reports to many unused variables. Read the `docs <https://github.com/jendrikseipp/vulture>`_ for more information.
