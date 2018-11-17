Dependencies
============

We use ``poetry`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.

Firstly, install ``poetry``, it is recommended to do so with ``curl``:

.. code:: bash

  POETRY_VERSION=0.12.8 curl -sSL "https://raw.githubusercontent.com/sdispater/poetry/${POETRY_VERSION}/get-poetry.py" | python

See below how to upgrade ``poetry`` version.


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

We use ``safety check`` to validate that we use only secure releases.
