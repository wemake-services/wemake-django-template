Dependencies
============

We use ``pipenv`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.

Firstly, install ``pipenv``, it is recommended to do so with ``pip3``:

.. code:: bash

  pip3 install pipenv


Installing all dependencies
---------------------------

Please, note that ``pipenv`` will automatically create a ``virtualenv`` for
this project. It will use ``python_verion`` specified in ``Pipfile``.
To install (or renew) all existing dependencies run:

.. code:: bash

  pipenv install -d


Installing dependencies for production use
------------------------------------------

To install dependencies for production use, you will need to run:

.. code:: bash

  pipenv install --ignore-pipfile

This command will fail if ``Pipfile.lock`` is missing, outdated or incorrect.


Activating virtualenv
---------------------

And to activate ``virtualenv`` created by ``pipenv`` run:

.. code:: bash

  pipenv shell


Adding new dependencies
-----------------------

To add a new dependency you can run:

- ``pipenv install django`` to install ``django`` as a production dependency
- ``pipenv install -d pytest`` to install ``pytest``
  as a development dependency


Dependencies security
---------------------

We use `pipenv check <https://docs.pipenv.org/advanced/#detection-of-security-vulnerabilities>`_ to validate that we use only secure releases.


Troubleshooting
---------------

There could be some common issues, like:

1. ``zsh: command not found: pip3``, it means that you don't have ``pip3`` installed. `Install <https://pip.pypa.io/en/stable/installing/>`_ it
2. When ``pipenv install`` returns error, head to `pipenv's issues <https://github.com/kennethreitz/pipenv/issues>`_ and create a new issue, use ``pip install`` in a while


Further reading
---------------

- `pipenv <https://docs.pipenv.org/>`_ docs
