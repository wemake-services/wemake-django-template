.. _tips:

Tips
====

This section is about some of the problems you may encounter and
how to solve these problems.

1. **The disk performance in Docker for Mac** - If you use the *Mac OS* you
know that you have problems with disk performance. Starting and restarting an
application is slower than with Linux (it's very noticeable for project with
large codebase). For particular solve this problem add `:delegated` to each
your volumes in `docker-compose.yaml`.

  .. code:: yaml

      volumes:
        - pgdata:/var/lib/postgresql/data:delegated

  For more information, you can look at the
  `docker documents <https://docs.docker.com/docker-for-mac/osxfs-caching/>`_ and
  a good `article <https://medium.com/@TomKeur/how-get-better-disk-performance-in-docker-for-mac-2ba1244b5b70>`_.
