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


Automatic dependencies update
-----------------------------

You can use `dependabot <https://github.com/dependabot/dependabot-script>`_
to enable automatic dependencies updates via Pull Requests to your repository.
Similar to the original template repository: `list of pull requests <https://github.com/wemake-services/wemake-django-template/pulls?q=is%3Apr+author%3Aapp%2Fdependabot>`_.

It is available to both Github and Gitlab.
But, for Gitlab version you currently have to update your `.gitlab-ci.yml <https://github.com/dependabot/dependabot-script/blob/master/.gitlab-ci.example.yml>`_.


Secret variables
----------------

If some real secret variables are required, then you can use `gitlab secrets <https://docs.gitlab.com/ee/ci/variables/#secret-variables>`_.
And these kind of variables are required *most* of the time.

See :ref:`django` on how to use ``dump-env`` and ``gitlab-ci`` together.


Documentation
-------------
After each deploy from master branch this documentation compiles into nice looking html page.
See `gitlab pages info <https://docs.gitlab.com/ee/user/project/pages/>`_.


Further reading
---------------

- `Container Registry <https://gitlab.com/help/user/project/container_registry>`_
- `Gitlab CI/CD <https://about.gitlab.com/features/gitlab-ci-cd/>`_
