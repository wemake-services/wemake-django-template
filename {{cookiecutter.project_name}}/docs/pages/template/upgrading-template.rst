Upgrading template
==================

Upgrading your project to be up-to-date with this template is a primary goal.
This is achieved by manually applying ``diff`` to your existing code.

``diff`` can be viewed from the project's ``README.md``.
See `an example <https://github.com/wemake-services/wemake-django-template/compare/91188fc4b89bd4989a0ead3d156a4619644965b0...master>`_.

When the upgrade is applied just change the commit hash in your template
to the most recent one.


Versions
--------

Sometimes, when we break something heavily, we create a version.
That is required for our users, so they can use old releases to create
projects as they used to be a long time ago.

However, we do not officially support older versions.
And we do not recommend to use them.

A full list of versions can be `found here <https://github.com/wemake-services/wemake-django-template/releases>`_.


Migration guides
----------------

Each time we create a new version, we also provide a migration guide.
What is a migration guide?
It is something you have to do to your project
other than just copy-pasting diffs from new versions.

Goodbye, poetry!
~~~~~~~~~~~~~~~~

This version requires a manual migration step.

1. You need to install ``uv``, see `uv installation <https://docs.astral.sh/uv/getting-started/installation/>`_
2. You need to convert your ``pyproject.toml`` dependencies from
   ``[tool.poetry.dependencies]`` to ``[project] dependencies`` (PEP 621 format)
3. You need to convert dev dependencies from
   ``[tool.poetry.group.dev.dependencies]`` to ``[dependency-groups] dev`` (PEP 735 format)
4. You need to remove the ``[build-system]`` section referencing ``poetry-core``
5. You need to remove all ``[tool.poetry]`` sections
6. Delete ``poetry.lock`` and run ``uv lock`` to generate ``uv.lock``
7. Update ``docker/django/Dockerfile`` to use ``uv`` instead of ``poetry``

You can use the `migrate-to-uv <https://github.com/mkniewallner/migrate-to-uv>`_
tool to automate most of these steps.

Goodbye, pipenv!
~~~~~~~~~~~~~~~~

This is an older migration step from ``pipenv`` to ``poetry``.

1. You need to install ``uv``
2. You need to create a new ``pyproject.toml`` file with ``uv init``
3. You need to adjust name, version, description, and authors meta fields
4. You need to copy-paste dependencies from ``Pipfile`` to ``pyproject.toml``
5. You need to set correct version for each dependency in the list,
   use ``">=x.y,<z.0"`` notation
6. Create ``uv.lock`` file with ``uv lock``

It should be fine! You may, however, experience some bugs related to different
dependency version resolution mechanisms. But, ``uv`` does it better.
