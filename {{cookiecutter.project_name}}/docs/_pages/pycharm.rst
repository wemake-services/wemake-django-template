PyCharm
=======

We are using ``PyCharm`` for development. It is an absolutely great tool.


Getting started
---------------

To setup your working environment you will need to run your ``docker-compose``:

.. code:: bash

   docker-compose up

And just leave it there up and running.


Running development server
--------------------------

Whenever you start a new project there will be several configurations available to you:

- ``runserver-docker``, which starts local ``docker-compose`` suited for development
- ``test-docker``, which starts tests on local ``docker-compose``

Just select any of these targets and execute them.


Deployment
----------

Deployment via ``PyCharm`` is not supported intentionally. And never will be.


Alternatives
------------

Some developers prefer to run local build without ``docker`` since it is faster and proven to be 100% stable.

It is now not configured by default. You have to configure it yourself.


Known issues
------------

- It may break in various parts, it is not 100% stable yet
- Your server will be available at ``http://127.0.0.1:8000/``, not ``http://0.0.0.0:8000/`` as ``PyCharm`` says
- It requires ``PyCharm 2017``, other versions will not work


Further reading
---------------

- ``PyCharm`` `docs <https://www.jetbrains.com/help/pycharm/docker-compose.html>`_
- `Configuring PyCharm remote hosts <https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-docker-compose.html>`_
