Documentation
=============

`We <https://github.com/wemake-services/meta>`_ write a lot of documentation.
Since we believe, that documentation is a crucial factor which defines project success or failure.

Here's how we write docs for ``django`` projects.


Dependencies
------------

We are using ``sphinx`` as a documentation builder.
We also use ``sphinx_autodoc_typehints`` to inject type annotations into docs.

We also using two sources of truth for the dependencies here:

- ``docs/requirements.txt``
- ``Pipfile``

Why? Because ReadTheDocs we are using for this template does only support traditional ``requirements.txt``.


Structure
---------

We structure our docs inside two folders:

- ``template`` - for everything connected to the template structure, contents, and general topic for all our projects. This folder should be the same for all our projects.
- ``project`` - this folder is project-specific. It contains the source code, instructions, architecture, decisions and other explanations.

Please, do not mix it up.


Further reading
---------------

- `sphinx <http://www.sphinx-doc.org/en/stable/>`_
- `sphinx with django <https://docs.djangoproject.com/en/1.11/internals/contributing/writing-documentation/#getting-started-with-sphinx>`_
- `sphinx-autodoc-typehints <https://github.com/agronholm/sphinx-autodoc-typehints>`_
