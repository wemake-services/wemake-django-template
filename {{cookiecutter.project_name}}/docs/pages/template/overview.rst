Overview
========

System requirements
-------------------

- ``git`` with version at least ``2.16`` or higher
- ``docker`` with version at least ``18.02`` or higher
- ``docker-compose`` with version at least ``1.21`` or higher


Container internals
-------------------

We use the ``docker-compose`` to link different containers together.
We also utilize different ``docker`` networks to control access.

Some containers might have long starting times, for example:

- ``postgres``
- ``rabbitmq``
- frontend, like ``node.js``

To be sure that container is started at the right time,
we utilize ``wait-for-command.sh`` script.
It is executed inside ``docker/django/entrypoint.sh`` file.

We start containers with ``tini``.
Because this way we have a proper signal handling
and eliminate zombie processes.
Read the `official docs <https://github.com/krallin/tini>`_ to know more.
