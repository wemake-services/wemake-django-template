Testing
=======

We try to keep our quality standards high.
So, we use different tools to make this possible.

We use `mypy <http://mypy-lang.org/>`_ for optional
static typing.
We run tests with `pytest <https://pytest.org/>`_ framework.


pytest
------

``pytest`` is the main tool for test discovery, collection, and execution.
It is configured inside ``setup.cfg`` file.

We use a lot of ``pytest`` plugins that enhance our development experience.
List of these plugins is available inside ``pyproject.toml`` file.

Running:

.. code:: bash

  pytest

We also have some options that are set on each run via ``--addopts``
inside the ``setup.cfg`` file.

Plugins
~~~~~~~

We use different ``pytest`` plugins to make our testing process better.
Here's the full list of things we use:

- `pytest-django`_ - plugin that introduces a lot of ``django`` specific
  helpers, fixtures, and configuration
- `django-test-migrations`_ - plugin to test Django migrations and their order
- `pytest-cov`_ - plugin to measure test coverage
- `covdefaults`_ - plugin for ``coverage`` to smartly ignore
  more meaningless lines.
- `pytest-randomly`_ - plugin to execute tests in random order and
  also set predictable random seed, so you can easily debug
  what went wrong for tests that rely on random behavior
- `pytest-timeout`_ - plugin to raise errors for tests
  that take too long to finish, this way you can control test execution speed

.. _pytest-django: https://github.com/pytest-dev/pytest-django
.. _django-test-migrations: https://github.com/wemake-services/django-test-migrations
.. _pytest-cov: https://github.com/pytest-dev/pytest-cov
.. _covdefaults: https://github.com/asottile/covdefaults
.. _pytest-randomly: https://github.com/pytest-dev/pytest-randomly
.. _pytest-timeout: https://pypi.org/project/pytest-timeout

Snapshot testing
~~~~~~~~~~~~~~~~

We use `inline-snapshot`_ to snapshot test values and
`inline-snapshot-django`_ to snapshot SQL queries directly in our test code.

This works as an advanced form of Django's ``assertNumQueries``:
it lets you see the actual query structure in your test and catch
regressions like N+1 queries or unintended changes in SQL.

To add snapshots to a test:

1. Wrap the code under test with ``snapshot_queries()``
2. Assert the result against an empty ``snapshot()``
3. Run the test — inline-snapshot fills in the captured queries automatically

.. code:: python

  from inline_snapshot import snapshot
  from inline_snapshot_django import snapshot_queries

  @pytest.mark.django_db
  def test_blog_post_get(dmr_client: DMRClient, blog_post: BlogPost) -> None:
      """Ensures that blog posts can be fetched."""
      with snapshot_queries() as snap:  # <---- Capture queries.
          response = dmr_client.get(
              reverse('api:main:blog_post_get', kwargs={'id': blog_post.pk}),
          )

      assert response.status_code == HTTPStatus.OK
      assert snap == snapshot()  # <---- Write empty, first run fills it.
      msgspec.convert(response.json(), type=BlogPostFullPayload)

After the first pytest run the snapshot will be updated in-place:

.. code:: python

      assert snap == snapshot([
          'SELECT ... FROM main_blogpost WHERE ... LIMIT ...',
      ])

When the expected output changes, update all snapshots with:

.. code:: bash

  pytest --inline-snapshot=fix

.. _inline-snapshot: https://github.com/15r10nk/inline-snapshot
.. _inline-snapshot-django: https://github.com/15r10nk/inline-snapshot-django

Tweaking tests performance
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several options you can provide or remove to make your tests faster:

- You can use ``pytest-xdist`` together with
  ``-n auto``  to schedule several numbers of workers,
  sometimes when there are a lot of tests it may increase the testing speed.
  But on a small project with a small amount of tests it just
  gives you an overhead, so removing it (together with ``--boxed``)
  will boost your testing performance
- If there are a lot of tests with database access
  it may be wise to add
  `--reuse-db option <https://pytest-django.readthedocs.io/en/latest/database.html#example-work-flow-with-reuse-db-and-create-db>`_,
  so ``django`` won't recreate database on each test
- If there are a lot of migrations to perform you may also add
  `--nomigrations option <https://pytest-django.readthedocs.io/en/latest/database.html#nomigrations-disable-django-1-7-migrations>`_,
  so ``django`` won't run all the migrations
  and instead will inspect and create models directly
- Removing ``coverage``. Sometimes that an option.
  When running tests in TDD style why would you need such a feature?
  So, coverage will be calculated when you will ask for it.
  That's a huge speed up
- Removing linters. Sometimes you may want to split linting and testing phases.
  This might be useful when you have a lot of tests, and you want to run
  linters before, so it won't fail your complex testing pyramid with a simple
  whitespace violation


mypy
----

Running ``mypy`` is required before any commit:

.. code:: bash

  mypy server tests/**/*.py

This will eliminate a lot of possible ``TypeError`` and other issues
in both ``server/`` and ``tests/`` directories.
We use ``tests/**/*.py`` because ``tests/`` is not a python package,
so it is not importable.

However, this will not make code 100% safe from errors.
So, both the testing and review process are still required.

``mypy`` is configured via ``setup.cfg``.
Read the `docs <https://mypy.readthedocs.io/en/latest/>`_
for more information.

We also use `django-stubs <https://github.com/typeddjango/django-stubs>`_
to type ``django`` internals.
This package is optional and can be removed,
if you don't want to type your ``django`` for some reason.
