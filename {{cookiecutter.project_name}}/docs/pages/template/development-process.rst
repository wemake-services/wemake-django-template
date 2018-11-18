Development process
===================

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


Local development
-----------------

When cloning a project for the first time you may
need to configure it properly,
see :ref:`django` section for more information.

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

Running project
~~~~~~~~~~~~~~~

If you have reached this point, you should be able to run the project.

.. code:: bash

  python manage.py runserver


Development with docker
-----------------------

To start development server inside ``docker`` you will need to run:

.. code:: bash

  docker-compose build
  docker-compose run --rm web python manage.py migrate
  docker-compose up

Running scripts inside docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As you have already mentioned inside the previous section
we use ``docker-compose run`` to run scripts inside docker.

What do you need to know about it?

1. You can run anything you want: ``poetry``, ``python``, ``sh``, etc
2. Most likely it will have a permanent effect, due to ``docker volumes``
3. You need to use ``--rm`` to automatically remove this container afterward

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
