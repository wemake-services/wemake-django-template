Development process
===================

Our development process is focused on high quality and development comfort.
We use tools that are proven to be the best in class.

Here are the steps to explain the process.


Setting up
----------

When cloning a project for the first time it may
need to configure it properly,
see :ref:`configuration` section for more information.

**Note**, that you only need to run these commands once per project.

Local database
~~~~~~~~~~~~~~

When using local development environment without ``docker``,
you will need a ``postgres`` up and running.
To create new development database run:

.. code:: bash

  psql postgres -f sql/create_database.sql

Then migrate your database:

.. code:: bash

  python manage.py migrate

You may also want to create a super user account:

.. code:: bash

  python manage.py createsuperuser

Configuring pre-commit
~~~~~~~~~~~~~~~~~~~~~~

We are using several pre-commit hooks to make sure everything works just fine.
Before you can run hooks, you need to have the pre-commit package installed.
It comes bundled in our project requirements (specified in ``Pipfile``).
To setup hooks after installing all the dependencies run:

.. code:: bash

  pre-commit install


You will now see the test results before any commit.
Before each commit the same testing routing as in CI
will be run on your machine.
Because we don't want to waste CI's and people's time
dealing with the fallen builds.

Running project
~~~~~~~~~~~~~~~

If you have reached this point, you should be able to run the project.

.. code:: bash

  python manage.py runserver


Making changes
--------------

When making changes into the project make sure
you write at least minimum ``unit``, ``doctest``, or integration test.
Also, check your coding style.

To run tests and style checks inside your ``virtualenv`` we use:

.. code:: bash

  pytest

See :ref:`linters` to know what style checks we use.


Tweaking tests performance
--------------------------

There are several options you can provide or remove to make your tests faster:

- ``-n auto`` is used to schedule several number of workers,
  sometimes when there are a lot of tests it may increase the testing speed.
  But on small project with small amount of test it just
  gives you an overhead, so removing it (together with `--boxed`)
  will boost your testing performance
- If there are a lot of tests with database access
  it may be wise to add
  `--reuse-db option <https://pytest-django.readthedocs.io/en/latest/database.html#example-work-flow-with-reuse-db-and-create-db>`_,
  so ``django`` won't recreate database on each test
- If there are a lot of migrations to perform you may also add
  `--nomigrations option <https://pytest-django.readthedocs.io/en/latest/database.html#nomigrations-disable-django-1-7-migrations>`_,
  so ``django`` won't run all the migrations
  and instead will inspect and create models directly
- Removing ``coverage``. Sometimes that an option.
  When running tests in TDD style why would you need such a feature?
  So, coverage will be calculated when you will ask for it.
  That's a huge speed up


Making a commit
---------------

Please, remember to write clean commit messages.
It should follow https://github.com/agis/git-style-guide


Quality
-------

We measure code quality and complexity with `radon <https://github.com/rubik/radon>`_. See :ref:`qa` to know more about ``QA``.
