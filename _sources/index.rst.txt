Welcome to wemake-django-template's documentation!
==================================================


What this project is all about?
The main idea of this project is to provide a fully configured
template for ``django`` projects, where code quality, testing,
documentation, security, and scalability are number one priorities.

This template is a result of implementing
`our processes <https://github.com/wemake-services/meta>`_,
it should not be considered as an independent part.


Goals
-----

When developing this template we had several goals in mind:

- Development environment should be bootstrapped easily,
  so we use ``docker-compose`` for that
- Development should be consistent, so we use strict quality and style checks
- Development, testing, and production should have the same environment,
  so again we develop, test, and run our apps in ``docker`` containers
- Documentation and codebase are the only sources of truth


Limitations
-----------

This project implies that:

- You are using ``docker`` for deployment
- You are using Gitlab and Gitlab CI
- You are not using any frontend assets in ``django``,
  you store your frontend separately


Should I choose this template?
------------------------------

This template is oriented on big projects,
when there are multiple people working on it for a long period of time.

If you want to simply create a working prototype without all these
limitations and workflows - feel free to choose any
`other template <https://github.com/audreyr/cookiecutter#python-django>`_.


How to start
------------

You should start with reading the documentation.
Reading order is important.

There are multiple processes that you need to get familiar with:

- First time setup phase: what system requirements you must fulfill,
  how to install dependencies, how to start your project
- Active development phase: how to make changes, run tests,


.. toctree::
   :maxdepth: 2
   :caption: Setting things up:

   pages/template/overview.rst
   pages/template/development.rst
   pages/template/django.rst

.. toctree::
   :maxdepth: 2
   :caption: Quality assurance:

   pages/template/documentation.rst
   pages/template/linters.rst
   pages/template/testing.rst
   pages/template/security.rst
   pages/template/gitlab-ci.rst

.. toctree::
   :maxdepth: 2
   :caption: Production:

   pages/template/production-checklist.rst
   pages/template/production.rst

.. toctree::
   :maxdepth: 1
   :caption: Extras:

   pages/template/upgrading-template.rst
   pages/template/faq.rst
   pages/template/troubleshooting.rst


Indexes and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
