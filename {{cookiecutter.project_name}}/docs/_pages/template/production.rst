Production
==========

We deploy our application using ``docker-compose`` files with version ``3`` and ``docker swarm``.


Setting up
----------

Creating a single file for deployment:

.. code:: bash

  docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml config > docker-compose.deploy.yml

Activating ``swarm`` mode (this command should be run only once per host):

.. code:: bash

  docker swarm init


Running
-------

To actually deploy a software run:

.. code:: bash

  docker stack deploy --compose-file docker-compose.deploy.yml my-app-name


Further readings
----------------

- Production with `docker-compose <https://docs.docker.com/compose/production>`_
- `docker-compose with swarm <https://docs.docker.com/compose/swarm/>`_
- `Full tutorial <https://docs.docker.com/get-started>`_
