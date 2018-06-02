Docker
======


Requirements
------------

``docker`` with version at least ``18.02`` or higher.


How does it work
----------------

We start containers with ``tini``.
Because this way we have a proper signal handling and no zombie processes.
Read the `official docs <https://github.com/krallin/tini>`_ to know more.

We use the standard way to link different containers together: `compose` files.
But, some containers might have long starting times, ``postgres`` for example.

To be sure that container is started at the time we start using it,
we utilize ``wait-for-command.sh`` script.


Development
-----------

To start development server inside ``docker`` you will need to run:

.. code:: bash

  docker-compose build
  docker-compose run web python manage.py migrate
  docker-compose up

You might want to tweak ``INTERNAL_IPS`` setting
to include ``docker`` container into it.
Otherwise ``django-debug-toolbar`` won't show up.

To get your ``docker`` ip run:

.. code:: bash

  docker inspect your-container-name | grep -e '"Gateway"'


Production
----------

You will need to specify extra configuration
to run ``docker-compose`` in production.
Since production build also uses ``caddy``,
which is not required into the development build.

.. code:: bash

  docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up -d


Going to production
-------------------

See :ref:`going-to-production` for more information.


Common issues
-------------

Pillow
~~~~~~

If you want to install ``Pillow`` that you should
add this to dockerfile and rebuild image:

- ``RUN apk add jpeg-dev zlib-dev``
- ``LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pipenv install ..."``

See `<https://github.com/python-pillow/Pillow/issues/1763>`_

Root owns build artifacts
~~~~~~~~~~~~~~~~~~~~~~~~~

This happens on some systems.
It happens because build happens in ``docker`` as the ``root`` user.
The fix is to pass current ``UID`` to ``docker``.
See `<https://github.com/wemake-services/wemake-django-template/issues/345>`_.


Further reading
---------------

- ``docker-compose`` `docs <https://docs.docker.com/compose/production/#modify-your-compose-file-for-production>`_
- ``caddy`` `tutorial <https://caddyserver.com/>`_
