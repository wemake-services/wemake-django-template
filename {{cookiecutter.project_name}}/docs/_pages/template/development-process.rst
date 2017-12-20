Development process
===================

Our development process is focused on high quality and development comfort.
We use tools that are proven to be the best in class.

Here are the steps to explain the process.


Setting up
----------

When cloning a project for the first time it may need to configure it properly, see :ref:`configuration` section for more information.

**Note**, that you only need to run these commands once per project.

Local database
~~~~~~~~~~~~~~

When using local development environment without ``docker``, you will need a ``postgres`` up and running. To create new development database run:

.. code:: bash

  psql postgres -f sql/create_database.sql

Then migrate your database:

.. code:: bash

  python manage.py migrate

Configuring pre-commit
~~~~~~~~~~~~~~~~~~~~~~

We are using several pre-commit hooks to make sure everything works just fine.
To setup hooks after installing all the dependencies run:

.. code:: bash

  pre-commit install


You will now see the test results before any commit. Before each commit the same testing routing as in CI will be run on your machine. Because we don't want to waste CI's and people's time dealing with the fallen build.


Making changes
--------------

When making changes into the project make sure you write at least minimum `unit` or integration test. Also, check your style.

To run tests and style checks inside your ``virtualenv`` we use:

.. code:: bash

  python -m pytest

See :ref:`linters` to know what style checks we use.


Making a commit
---------------

Please, remember to write clean commit messages. It should follow https://github.com/agis/git-style-guide


Quality
-------

We measure code quality and complexity with `radon <https://github.com/rubik/radon>`_. See :ref:`qa` to know more about ``QA``.
