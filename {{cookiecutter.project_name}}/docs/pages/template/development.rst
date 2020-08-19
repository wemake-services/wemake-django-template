Development
===========

Our development process is focused on high quality and development comfort.
We use tools that are proven to be the best in class.

There are two possible ways to develop your apps.

1. local development
2. development inside ``docker``

You can choose one or use both at the same time.
How to choose what method should you use?

Local development is much easier and much faster.
You can choose it if you don't have too many infrastructure dependencies.
That's a default option for the new projects.

Choosing ``docker`` development means that you already have a complex
setup of different technologies, containers, networks, etc.
This is a default option for older and more complicated projects.


Dependencies
------------

We use ``poetry`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.
Before going any further, please,
take a moment to read the `official documentation <https://poetry.eustace.io/>`_
about ``poetry`` to know some basics.

If you are using ``docker`` then prepend ``docker-compose run --rm web``
before any of those commands to execute them.

Please, note that you don't need almost all of them with ``docker``.
You can just skip this sub-section completely.
Go right to `Development with docker`_.

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

You do not need to run any of these command for ``docker`` based development,
since it is already executed inside ``Dockerfile``.

Please, note that ``poetry`` will automatically create a ``virtualenv`` for
this project. It will use you current ``python`` version.
To install all existing dependencies run:

.. code:: bash

  poetry install

To install dependencies for production use, you will need to run:

.. code:: bash

  poetry install --no-dev

And to activate ``virtualenv`` created by ``poetry`` run:

.. code:: bash

  poetry shell

Adding new dependencies
~~~~~~~~~~~~~~~~~~~~~~~

To add a new dependency you can run:

- ``poetry add django`` to install ``django`` as a production dependency
- ``poetry add --dev pytest`` to install ``pytest``
  as a development dependency

This command might be used with ``docker``.

Updating poetry version
~~~~~~~~~~~~~~~~~~~~~~~

Package managers should also be pinned very strictly.
We had a lot of problems in production
because we were not pinning package manager versions.

This can result in broken ``lock`` files, inconsistent installation process,
bizarre bugs, and missing packages. You do not want to experience that!

How can we have the same ``poetry`` version for all users in a project?
That's where ``[build-system]`` tag shines. It specifies the exact version of
your ``poetry`` installation that must be used for the project.
Version mismatch will fail your build.

When you want to update ``poetry``, you have to bump it in several places:

1. ``pyproject.toml``
2. ``docker/django/Dockerfile``

Then you are fine!


Development with docker
-----------------------

To start development server inside ``docker`` you will need to run:

.. code:: bash

  docker-compose build
  docker-compose run --rm web python manage.py migrate
  docker-compose up

Running scripts inside docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we have already mentioned inside the previous section
we use ``docker-compose run`` to run scripts inside docker.

What do you need to know about it?

1. You can run anything you want: ``poetry``, ``python``, ``sh``, etc
2. Most likely it will have a permanent effect, due to ``docker volumes``
3. You need to use ``--rm`` to automatically remove this container afterward

**Note**: ``docker`` commands do not need to use ``virtualenv`` at all.

Extra configuration
~~~~~~~~~~~~~~~~~~~

You might want to tweak ``INTERNAL_IPS`` ``django`` setting
to include your ``docker`` container address into it.
Otherwise ``django-debug-toolbar`` might not show up.

To get your ``docker`` ip run:

.. code:: bash

  docker inspect your-container-name | grep -e '"Gateway"'

You can also configure a permanent hostname inside your ``/etc/hosts`` to
access your ``docker`` containers with a permanent hostname.


Local development
-----------------

When cloning a project for the first time you may
need to configure it properly,
see :ref:`django` section for more information.

**Note**, that you will need to activate ``virtualenv`` created
by ``poetry`` before running any of these commands.
**Note**, that you only need to run these commands once per project.

Local database
~~~~~~~~~~~~~~

When using local development environment without ``docker``,
you will need a ``postgres`` up and running.
To create new development database run
(make sure that database and user names are correct for your case):

.. code:: bash

  psql postgres -U postgres -f sql/create_database.sql

Then migrate your database:

.. code:: bash

  python manage.py migrate

Running project
~~~~~~~~~~~~~~~

If you have reached this point, you should be able to run the project.

.. code:: bash

  python manage.py runserver
