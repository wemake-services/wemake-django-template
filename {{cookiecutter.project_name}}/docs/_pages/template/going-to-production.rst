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


Postgres
--------

Sometimes using ``postgres`` inside a container `is not a good idea <https://myopsblog.wordpress.com/2017/02/06/why-databases-is-not-for-containers/>`_.
So, what should be done in this case?

First of all, move your database ``docker`` service definition inside ``docker-compose.override.yml``. Doing so will not affect development, but will remove database service from production.
Next, you will need to specify `extra_hosts <https://docs.docker.com/compose/compose-file/#extra_hosts>`_ to contain your ``postgresql`` address.
Lastly, you would need to add new hosts to ``pg_hba.conf``.

`Here <http://winstonkotzan.com/blog/2017/06/01/connecting-to-external-postgres-database-with-docker.html>`_'s a nice tutorial about this topic.


Caddy
-----

Let's Encrypt
~~~~~~~~~~~~~

We are using ``Caddy`` and ``Let's Encrypt`` for HTTPS.
The Caddy webserver used in the default configuration will get you a valid certificate from ``Let's Encrypt`` and update it automatically. All you need to do to enable this is to make sure that your DNS records are pointing to the server Caddy runs on.

Read more: `Automatic HTTPS <https://caddyserver.com/docs/automatic-https>`_ in Caddy docs.

Disabling HTTPS
~~~~~~~~~~~~~~~

You would need to `disable <https://caddyserver.com/docs/tls>`_ ``https`` inside ``Caddy`` and in production settings for Django. Because Django itself also redirects to `https`. See `docs <https://docs.djangoproject.com/en/1.11/ref/settings/#secure-ssl-redirect>`_.

You would also need to disable ``manage.py check`` in ``docker/django/gunicorn.sh``. Otherwise your application won't start, it would not pass ``django``'s security checks.

Disabling WWW subdomain
~~~~~~~~~~~~~~~~~~~~~~~

If you for some reason do not require ``www.`` subdomain, then delete ``www.{$DOMAIN_NAME}`` section from ``Caddyfile``.


Further reading
---------------

- Django's deployment `checklist <https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#deployment-checklist>`_
