.. _`going-to-production`:

Going to production
===================

This section covers everything you need to know before going to production.


Check
-----

Before going to production make sure you have checked everything:

.. code:: bash

  DJANGO_ENV=production python manage.py check --deploy

This command should give not warnings or errors. It is bundled into `docker`, so container will not work with any warnings.


Caddy and Let's Encrypt
-----------------------

We are using ``Caddy`` and ``Let's Encrypt`` for HTTPS.
The Caddy webserver used in the default configuration will get you a valid certificate from ``Let's Encrypt`` and update it automatically. All you need to do to enable this is to make sure that your DNS records are pointing to the server Caddy runs on.

Read more: `Automatic HTTPS <https://caddyserver.com/docs/automatic-https>`_ in Caddy docs.


Further reading
---------------

- ``Django``'s deployment checklist_

.. _checklist: https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#deployment-checklist
