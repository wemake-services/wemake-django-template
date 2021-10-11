.. _`going-to-production`:

Going to production
===================

This section covers everything you need to know before going to production.


Django
------

Checks
~~~~~~

Before going to production make sure you have checked everything:

1. Migrations are up-to-date
2. Static files are all present
3. There are no security or other ``django`` warnings

Checking migrations, static files,
and security is done inside ``ci.sh`` script.

We check that there are no unapplied migrations:

.. code :: bash

  python manage.py makemigrations --dry-run --check

If you have forgotten to create a migration and changed the model,
you will see an error on this line.

We also check that static files can be collected:

.. code :: bash

   DJANGO_ENV=production python manage.py collectstatic --no-input --dry-run

However, this check does not cover all the cases.
Sometimes ``ManifestStaticFilesStorage`` will fail on real cases,
but will pass with ``--dry-run`` option.
You can disable ``--dry-run`` option if you know what you are doing.
Be careful with this option, when working with auto-uploading
your static files to any kind of CDNs.

That's how we check ``django`` warnings:

.. code:: bash

  DJANGO_ENV=production python manage.py check --deploy --fail-level WARNING

These warnings are raised by ``django``
when it detects any configuration issues.

This command should give not warnings or errors.
It is bundled into ``docker``, so the container will not work with any warnings.

Static and media files
~~~~~~~~~~~~~~~~~~~~~~

We use ``/var/www/django`` folder to store our media
and static files in production as ``/var/www/django/static``
and ``/var/www/django/media``.
Docker uses these two folders as named volumes.
And later these volumes are also mounted to ``caddy``
with ``ro`` mode so it possible to read their contents.

To find the exact location of these files on your host
you will need to do the following:

.. code:: bash

  docker volume ls  # to find volumes' names
  docker volume inspect VOLUME_NAME

Sometimes storing your media files inside a container is not a good idea.
Use ``CDN`` when you have a lot of user content
or it is very important not to lose it.
There are `helper libraries <http://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html>`_
to bind ``django`` and these services.

If you don't need ``media`` files support, just remove the volumes.

Migrations
~~~~~~~~~~

We do run migration in the ``gunicorn.sh`` by default.
Why do we do this? Because that's probably the easiest way to do it.
But it clearly has some disadvantages:

- When scaling your container for multiple nodes you will have multiple
  threads running the same migrations. And it might be a problem since
  migrations do not guarantee that it will work this way.
- You can perform some operations multiple times
- Possible other evil things may happen

So, what to do in this case?
Well, you can do whatever it takes to run migrations in a single thread.
For example, you can create a separate container to do just that.
Other options are fine as well.


Postgres
--------

Sometimes using ``postgres`` inside a container
`is not a good idea <https://myopsblog.wordpress.com/2017/02/06/why-databases-is-not-for-containers/>`_.
So, what should be done in this case?

First of all, move your database ``docker`` service definition
inside ``docker-compose.override.yml``.
Doing so will not affect development,
but will remove database service from production.
Next, you will need to specify `extra_hosts <https://docs.docker.com/compose/compose-file/#extra_hosts>`_
to contain your ``postgresql`` address.
Lastly, you would need to add new hosts to ``pg_hba.conf``.

`Here <http://winstonkotzan.com/blog/2017/06/01/connecting-to-external-postgres-database-with-docker.html>`_
is a nice tutorial about this topic.


Caddy
-----

Let's Encrypt
~~~~~~~~~~~~~

We are using ``Caddy`` and ``Let's Encrypt`` for HTTPS.
The Caddy webserver used in the default configuration will get
you a valid certificate from ``Let's Encrypt`` and update it automatically.
All you need to do to enable this is to make sure
that your DNS records are pointing to the server Caddy runs on.

Read more: `Automatic HTTPS <https://caddyserver.com/docs/automatic-https>`_
in Caddy docs.

Caddyfile validation
~~~~~~~~~~~~~~~~~~~~

You can also run ``-validate`` command to validate ``Caddyfile`` contents.

Here's it would look like:

.. code:: bash

  docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml
  run --rm caddy -validate

This check is not included in the pipeline by default,
because it is quite long to start all the machinery for this single check.

Disabling HTTPS
~~~~~~~~~~~~~~~

You would need to `disable <https://caddyserver.com/docs/tls>`_
``https`` inside ``Caddy`` and in production settings for Django.
Because Django itself also redirects to ``https``.
See `docs <https://docs.djangoproject.com/en/3.2/ref/settings/#secure-ssl-redirect>`_.

You would also need to disable ``manage.py check``
in ``docker/ci.sh``.
Otherwise, your application won't start,
it would not pass ``django``'s security checks.

Disabling WWW subdomain
~~~~~~~~~~~~~~~~~~~~~~~

If you for some reason do not require ``www.`` subdomain,
then delete ``www.{$DOMAIN_NAME}`` section from ``Caddyfile``.

Third-Level domains
~~~~~~~~~~~~~~~~~~~

You have to disable ``www`` subdomain if
your app works on third-level domains like:

- ``kira.wemake.services``
- ``support.myapp.com``

Otherwise, ``Caddy`` will server redirects to ``www.example.yourdomain.com``.


Further reading
---------------

- Django's deployment `checklist <https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#deployment-checklist>`_
