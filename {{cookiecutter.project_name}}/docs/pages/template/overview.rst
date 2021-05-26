Overview
========


System requirements
-------------------

- ``git`` with a version at least ``2.16`` or higher
- ``docker`` with a version at least ``18.02`` or higher
- ``docker-compose`` with a version at least ``1.21`` or higher
- ``python`` with exact version, see ``pyproject.toml``


Architecture
------------

config
~~~~~~

- ``config/.env.template`` - a basic example of what keys must be contained in
  your ``.env`` file, this file is committed to VCS
  and must not contain private or secret values
- ``config/.env`` - main file for secret configuration,
  contains private and secret values, should not be committed to VCS

root project
~~~~~~~~~~~~

- ``README.md`` - main readme file, it specifies the entry
  point to the project's documentation
- ``.dockerignore`` - specifies what files should not be
  copied to the ``docker`` image
- ``.editorconfig`` - file with format specification.
  You need to install the required plugin for your IDE in order to enable it
- ``.gitignore`` - file that specifies
  what should we commit into the repository and we should not
- ``.gitlab-ci.yml`` - GitLab CI configuration file.
  It basically defines what to do with your project
  after pushing it to the repository. Currently it is used for testing
  and releasing a ``docker`` image
- ``docker-compose.yml`` - this the file specifies ``docker`` services
  that are needed for development and testing
- ``docker-compose.override.yml`` - local override for ``docker-compose``.
  Is applied automatically and implicitly when
  no arguments provided to ``docker-compose`` command
- ``manage.py`` - main file for your ``django`` project.
  Used as an entry point for the ``django`` project
- ``pyproject.toml`` - main file of the project.
  It defines the project's dependencies.
- ``poetry.lock`` - lock file for dependencies.
  It is used to install exactly the same versions of dependencies on each build
- ``setup.cfg`` - configuration file, that is used by all tools in this project
- ``locale/`` - helper folder, that is used to store locale data,
  empty by default
- ``sql/`` - helper folder, that contains ``sql`` script for database setup
  and teardown for local development

server
~~~~~~

- ``server/__init__.py`` - package definition, empty file
- ``server/urls.py`` - ``django`` `urls definition <https://docs.djangoproject.com/en/3.2/topics/http/urls/>`_
- ``server/wsgi.py`` - ``django`` `wsgi definition <https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface>`_
- ``server/asgi.py`` - ``django`` `asgi definition <https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface>`_
- ``server/apps/`` - place to put all your apps into
- ``server/apps/main`` - ``django`` application, used as an example,
  could be removed
- ``server/settings`` - settings defined with ``django-split-settings``,
  see this `tutorial <https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d>`_
  for more information
- ``server/templates`` - external folder for ``django`` templates,
  used for simple files as ``robots.txt`` and so on

docker
~~~~~~

- ``docker/ci.sh`` - file that specifies all possible checks that
  we execute during our CI process
- ``docker/docker-compose.prod.yml`` - additional service definition file
  used for production
- ``docker/django/Dockerfile`` - ``django`` container definition,
  used both for development and production
- ``docker/django/entrypoint.sh`` - entry point script that is used
  when ``django`` container is starting
- ``docker/django/gunicorn.sh`` - production script for ``django``,
  that's how we configure ``gunicorn`` runner
- ``docker/caddy/Caddyfile`` - configuration file for Caddy webserver

tests
~~~~~

- ``tests/test_server`` - tests that ensures that basic ``django``
  stuff is working, should not be removed
- ``tests/test_apps/test_main`` - example tests for the ``django`` app,
  could be removed
- ``tests/conftest.py`` - main configuration file for ``pytest`` runner

docs
~~~~

- ``docs/Makefile`` - command file that builds the documentation for Unix
- ``docs/make.bat`` - command file for Windows
- ``docs/conf.py`` - ``sphinx`` configuration file
- ``docs/index.rst`` - main documentation file, used as an entry point
- ``docs/pages/project`` - folder that will contain
  documentation written by you!
- ``docs/pages/template`` - folder that contains documentation that
  is common for each project built with this template
- ``docs/documents`` - folder that should contain any documents you have:
  spreadsheets, images, requirements, presentations, etc
- ``docs/requirements.txt`` - helper file, contains dependencies
  for ``readthedocs`` service. Can be removed
- ``docs/README.rst`` - helper file for this directory,
  just tells what to do next


Container internals
-------------------

We use the ``docker-compose`` to link different containers together.
We also utilize different ``docker`` networks to control access.

Some containers might have long starting times, for example:

- ``postgres``
- ``rabbitmq``
- frontend, like ``node.js``

To be sure that container is started at the right time,
we utilize ``dockerize`` `script <https://github.com/jwilder/dockerize>`_.
It is executed inside ``docker/django/entrypoint.sh`` file.

We start containers with ``tini``.
Because this way we have a proper signal handling
and eliminate zombie processes.
Read the `official docs <https://github.com/krallin/tini>`_ to know more.
