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
