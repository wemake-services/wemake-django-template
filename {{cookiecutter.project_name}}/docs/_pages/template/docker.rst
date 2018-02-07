Docker
======


Requirements
------------

``docker`` with version at least ``17.07`` or higher.


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
- ``LIBRARY_PATH=/lib:/usr/lib /bin/sh -c
  "test "$DJANGO_ENV" == production && pipenv install
  --system --ignore-pipfile || pipenv install --dev
  --system --ignore-pipfile"``

See `<https://github.com/python-pillow/Pillow/issues/1763>`_


Further reading
---------------

- ``docker-compose`` `docs <https://docs.docker.com/compose/production/#modify-your-compose-file-for-production>`_
- ``caddy`` `tutorial <https://caddyserver.com/>`_
