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
- You should not push broken code to the repo,
  so we use ``pre-commit`` hooks for that
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
`other templates <https://github.com/audreyr/cookiecutter#python-django>`_.


How to start
------------

This project is created to be well documented.
You should start with reading the documentation.
It is available
`online <http://wemake-django-template.readthedocs.io/en/latest>`_.
Reading order is important.

To sum up all the steps, you will have to:

1. Install dependencies
2. Configure a project itself and IDE
3. Run and test your application
4. Know how to make changes
5. Commit your code and receive a feedback


Upgrading template
------------------

Upgrading your project to be up-to-date with this template is a primary goal.
This is achieved by manually applying ``diff`` to your existing code.

``diff`` can be viewed from the project's ``README.md``.
See `an example <https://github.com/wemake-services/wemake-django-template/compare/91188fc4b89bd4989a0ead3d156a4619644965b0...master>`_.

When upgrade is applied just change the commit hash in your template
to the most recent one.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   _pages/template/dependencies.rst
   _pages/template/configuration.rst
   _pages/template/development-process.rst
   _pages/template/linters.rst
   _pages/template/qa.rst
   _pages/template/documentation.rst
   _pages/template/pycharm.rst
   _pages/template/docker.rst
   _pages/template/gitlab-ci.rst
   _pages/template/going-to-production.rst
   _pages/template/production.rst


Indexes and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
