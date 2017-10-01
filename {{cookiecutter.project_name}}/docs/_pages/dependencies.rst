Dependencies
============

We use ``pipenv`` to manage dependencies. So, please do not use ``virtualenv`` or ``pip`` directly.

Firstly, install ``pipenv``, it is recommended to do so with `pipsi`_:

.. _pipsi: https://github.com/mitsuhiko/pipsi

.. code:: bash

  pip install pipsi
  pipsi install pew
  pipsi install pipenv


Installing all dependencies
---------------------------

Please, note that ``pipenv`` will automatically create a ``virtualenv`` for
this project. It will use ``python_verion`` specified in ``Pipfile``.
To install (or renew) all existing dependencies run:

.. code:: bash

  pipenv install -d


Installing production dependencies only
---------------------------------------

To install dependencies for production use, you will need to run:

.. code:: bash

  pipenv install --deploy

This command will fail if ``Pipfile.lock`` is missing or incorrect.


Activating virtualenv
---------------------

And to activate ``virtualenv`` created by ``pipenv`` run:

.. code:: bash

  pipenv shell


Adding new dependencies
-----------------------

To add a new dependency you can run:

- ``pipenv install django`` to install ``django`` as a production dependency
- ``pipenv install -d ipython`` to install ``ipython`` as a development dependency


Further reading
---------------

- ``pipenv`` `docs`_

.. _docs: https://docs.pipenv.org/
