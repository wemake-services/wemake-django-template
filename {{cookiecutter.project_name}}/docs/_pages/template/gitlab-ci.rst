Gitlab CI
=========

We use ``Gitlab CI`` to build our containers, test it,
and store them in the internal registry.

These images are then pulled into the production servers.


Configuration
-------------

All configuration is done inside ``.gitlab-ci.yml``.


Secret variables
----------------

If some real secret variables are required, then you can use `gitlab secrets <https://docs.gitlab.com/ee/ci/variables/#secret-variables>`_.


Slack webhooks
--------------

We utilize ``slack`` to receive notifications about
different events happened to our repository.

Read the `docs <https://docs.gitlab.com/ee/user/project/integrations/slack.html>`_ about how to achieve this.


Further reading
---------------

- `Container Registry <https://gitlab.com/help/user/project/container_registry>`_
- `Gitlab CI <https://about.gitlab.com/features/gitlab-ci-cd/>`_
