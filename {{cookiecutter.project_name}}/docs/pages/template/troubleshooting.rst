Troubleshooting
===============

This section is about some of the problems you may encounter and
how to solve these problems.


Docker
------

Pillow
~~~~~~

If you want to install ``Pillow`` that you should
add this to dockerfile and rebuild image:

- ``RUN apk add jpeg-dev zlib-dev``
- ``LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "poetry install ..."``

See `<https://github.com/python-pillow/Pillow/issues/1763>`_

Root owns build artifacts
~~~~~~~~~~~~~~~~~~~~~~~~~

This happens on some systems.
It happens because build happens in ``docker`` as the ``root`` user.
The fix is to pass current ``UID`` to ``docker``.
See `<https://github.com/wemake-services/wemake-django-template/issues/345>`_.

MacOS performance
~~~~~~~~~~~~~~~~~

If you use the MacOS you
know that you have problems with disk performance.
Starting and restarting an application is slower than with Linux
(it's very noticeable for project with large codebase).
For particular solve this problem add ``:delegated`` to each
your volumes in ``docker-compose.yml`` file.

.. code:: yaml

  volumes:
    - pgdata:/var/lib/postgresql/data:delegated

For more information, you can look at the
`docker documents <https://docs.docker.com/docker-for-mac/osxfs-caching/>`_
and a good `article <https://medium.com/@TomKeur/how-get-better-disk-performance-in-docker-for-mac-2ba1244b5b70>`_.
