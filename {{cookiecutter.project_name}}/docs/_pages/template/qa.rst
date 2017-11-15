.. _qa:

QA
==

We are using `radon <https://github.com/rubik/radon>`_ and `xenon <https://github.com/rubik/xenon>`_ to measure code complexity and quality.


Rules
-----

Here are our standards:

- A single block of code can not go below ``B`` mark
- A single module can not go below ``A`` mark
- Overall mark can not go below ``A`` mark

If your commit breaks this rule: well, the build won't succeed.


Running code analysis
---------------------

There are several metrics we use.

Cyclomatic Comlexity:

.. code:: bash

  radon cc . -a

Maintainability Index:

.. code:: bash

  radon mi .

And at last raw metrics:

.. code:: bash

  radon raw .


Running validation
------------------

If you would like to run QA by hand:

.. code:: bash

  xenon --max-absolute B --max-modules A --max-average A .

It will return status code ``0`` if everything is fine.
