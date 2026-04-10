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

We use ``uv`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.
Before going any further, please,
take a moment to read the `official documentation <https://docs.astral.sh/uv/>`_
about ``uv`` to know some basics.

If you are using ``docker`` then prepend ``docker compose run --rm web``
before any of those commands to execute them.

Please, note that you don't need almost all of them with ``docker``.
You can just skip this sub-section completely.
Go right to `Development with docker`_.

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

You do not need to run any of these commands for ``docker`` based development,
since it is already executed inside ``Dockerfile``.

Please, note that ``uv`` will automatically create a ``.venv`` for
this project. It will use your current ``python`` version.
To install all existing dependencies run:

.. code:: bash

  uv sync

To install dependencies for production use, you will need to run:

.. code:: bash

  uv sync --no-dev

To install all dependencies, including docs:

.. code:: bash

  uv sync --group docs

And to activate ``virtualenv`` created by ``uv`` run:

.. code:: bash

  . .venv/bin/activate

Adding new dependencies
~~~~~~~~~~~~~~~~~~~~~~~

To add a new dependency you can run:

- ``uv add django`` to install ``django`` as a production dependency
- ``uv add --group dev pytest`` to install ``pytest``
  as a development dependency
- ``uv add --group docs some-sphinx-plugin`` to install ``some-sphinx-plugin``
  as a documentation dependency

This command might be used with ``docker``.

Updating uv version
~~~~~~~~~~~~~~~~~~~~

The ``uv`` version is pinned in ``docker/django/Dockerfile``
via the ``COPY --from=ghcr.io/astral-sh/uv:<version>`` directive.
When you want to update ``uv``, bump the version tag there.


Development with docker
-----------------------

To start development server inside ``docker`` you will need to run:

.. code:: bash

  export DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 # enable buildkit
  docker compose build
  docker compose run --rm web python manage.py migrate
  docker compose up

Running scripts inside docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we have already mentioned inside the previous section
we use ``docker compose run`` to run scripts inside docker.

What do you need to know about it?

1. You can run anything you want: ``uv``, ``python``, ``sh``, etc
2. Most likely it will have a permanent effect, due to ``docker volumes``
3. You need to use ``--rm`` to automatically remove this container afterward

**Note**: ``docker`` commands do not need to use ``virtualenv`` at all.

Local development
-----------------

When cloning a project for the first time you may
need to configure it properly,
see :ref:`django` section for more information.

**Note**, that you will need to activate ``virtualenv`` created
by ``uv`` before running any of these commands.
**Note**, that you only need to run these commands once per project.

Local database
~~~~~~~~~~~~~~

When using local development environment without ``docker``,
you will need a ``postgres`` up and running.
To create new development database run
(make sure that database and user names are correct for your case):

.. code:: bash

  psql postgres -U postgres -f scripts/create_dev_database.sql

Then migrate your database:

.. code:: bash

  python manage.py migrate

Running project
~~~~~~~~~~~~~~~

If you have reached this point, you should be able to run the project.

.. code:: bash

  python manage.py runserver
