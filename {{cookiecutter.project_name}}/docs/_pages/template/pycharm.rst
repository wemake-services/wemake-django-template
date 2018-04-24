PyCharm
=======

We are using ``PyCharm`` for development.
It is an absolutely great tool.

``pycharm`` is a paid tool.
But, you can download a free `trial version <https://www.jetbrains.com/pycharm/download>`_.


One time setup
--------------

You will need to do a one time setup when you start to work
on a project for the first time.

editorconfig
~~~~~~~~~~~~

Firstly, you will need to install ``editorconfig`` plugin.
Go to: Settings -> Plugins.
Then search for ``editoconfig`` and install it.
You may need to restart a ``pycharm``.

Docker
~~~~~~

Secondly, you will need to create a remote ``docker`` interpreter
for ``pycharm`` to run your code.

- Go to: `Settings -> Project -> Project Interpreter -> Add Remote`
- Then select "Docker Compose"
- Select `docker-compose.yml` and `docker-compose.override.yml`
  as configuration files and `web` as a service
- You are done

This project ships with prebuild configuration for development
server and tests.
So, when interpreter will be ready, you can
hit ``runserver-docker`` to start the server.
Everything should run correctly.


Running
-------

Whenever you start a new project there will be several
configurations available to you:

- ``runserver-docker``, which starts local ``docker-compose``
  with ``python manage.py runserver`` command
- ``test-docker``, which starts tests on local ``docker-compose``

Just select any of these targets and execute them.
Or create some extra commands for things that you need.


Deployment
----------

Deployment via ``PyCharm`` is not supported intentionally.
And never will be.


Alternatives
------------

Some developers prefer to run local build without ``docker``
since it is faster and proven to be 100% stable.

It is now not configured by default.
You have to configure it yourself.


Known issues
------------

- It may break in various parts, it is not 100% stable yet
- Your server will be available at ``http://127.0.0.1:8000/``,
  not ``http://0.0.0.0:8000/`` as ``PyCharm`` says
- It requires ``PyCharm 2017`` or newer, other versions will not work
- When trying to debug tests you will need to disable ``pytest-cov`` by
  removing ``--cov`` options from ``setup.cfg``. They do not play well


Further reading
---------------

- ``PyCharm`` `docs <https://www.jetbrains.com/help/pycharm/docker-compose.html>`_
- `Configuring PyCharm remote hosts <https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-docker-compose.html>`_
