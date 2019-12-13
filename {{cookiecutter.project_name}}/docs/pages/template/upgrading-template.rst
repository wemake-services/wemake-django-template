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
That's is required for our users, so they can use old releases to create
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

Goodbye, pipenv!
~~~~~~~~~~~~~~~~

This version requires a manual migration step.

1. You need to install ``poetry``
2. You need to create a new ``pyproject.toml`` file with ``poetry init``
3. You need to adjust name, version, description, and authors meta fields
4. You need to copy-paste dependencies from ``Pipfile`` to ``pyproject.toml``
5. You need to set correct version for each dependency in the list,
   use ``"^x.y"`` `notation <https://github.com/python-poetry/poetry#caret-requirement>`_
6. You need to adjust ``[build-system]`` tag and ``POETRY_VERSION`` variable
   to fit your ``poetry`` version
7. Create ``poetry.lock`` file with ``poetry lock``

It should be fine! You may, however, experience some bugs related to different
dependency version resolution mechanisms. But, ``poetry`` does it better.
