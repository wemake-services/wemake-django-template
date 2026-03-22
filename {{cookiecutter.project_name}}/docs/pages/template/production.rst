Production
==========

We use different tools and setup for production.
We do not fully provide this part with the template. Why?

1. It requires a lot of server configuration
2. It heavily depends on your needs: performance, price, technology, etc
3. It is possible to show some vulnerable parts to possible attackers

So, you will need to deploy your application by yourself.
Here, we would like to cover some basic things that are not changed
from deployment strategy.

The easiest deployment strategy for small apps is ``docker-compose`` and
``systemd`` inside a host operating system.


Production configuration
------------------------

You will need to specify extra configuration
to run ``docker-compose`` in production.
Since production build also uses ``caddy``,
which is not required in the development build.

.. code:: bash

  docker compose -f docker-compose.yml -f docker/docker-compose.prod.yml up


Pulling pre-built images
------------------------

You will need to pull pre-built images from ``Gitlab`` to run them.
How to do that?

The first step is to create a personal access token for this service.
Then, login into your registry with:

.. code:: bash

   docker login registry.gitlab.your.domain

And now you are ready to pull your images:

.. code:: bash

   docker pull your-image:latest

See `official Gitlab docs <https://docs.gitlab.com/ee/user/packages/container_registry/>`_.


Updating already running service
--------------------------------

If you deploy with ``docker compose`` on a single host, update by pulling
new images and recreating containers:

.. code:: bash

   docker compose -f docker-compose.yml -f docker/docker-compose.prod.yml pull
   docker compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d

If you build images on the server instead of pulling pre-built ones,
rebuild and recreate:

.. code:: bash

   docker compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d --build

See `docker compose up <https://docs.docker.com/reference/cli/docker/compose/up/>`_.

Zero-Time Updates
~~~~~~~~~~~~~~~~~

Zero-Time Updates can be tricky.
You need to create containers with the new code, update existing services,
wait for the working sessions to be completed, and to shut down old
containers.


Further reading
---------------

- Production with `docker compose <https://docs.docker.com/compose/production>`_
- `Full tutorial <https://docs.docker.com/get-started>`_
