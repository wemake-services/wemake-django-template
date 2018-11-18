Gitlab CI
=========

We use ``Gitlab CI`` to build our containers, test it,
and store them in the internal registry.

These images are then pulled into the production servers.


Configuration
-------------

All configuration is done inside ``.gitlab-ci.yml``.


Pipelines
---------

We have two pipelines configured: for ``master`` and other branches.
That's how it works: we only run testing for feature branches and do the whole
building/testing/deploying process for the ``master`` branch.

This allows us to speed up development process.


Secret variables
----------------

If some real secret variables are required, then you can use `gitlab secrets <https://docs.gitlab.com/ee/ci/variables/#secret-variables>`_.
And these kind of variables are required *most* of the time.

See :ref:`django` on how to use ``dump-env`` and ``gitlab-ci`` together.


Further reading
---------------

- `Container Registry <https://gitlab.com/help/user/project/container_registry>`_
- `Gitlab CI/CD <https://about.gitlab.com/features/gitlab-ci-cd/>`_
