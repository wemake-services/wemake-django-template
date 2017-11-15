Welcome to wemake-django-template's documentation!
==================================================

.. include:: _pages/quickstart.rst

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   _pages/template/dependencies.rst
   _pages/template/configuration.rst
   _pages/template/development-process.rst
   _pages/template/linters.rst
   _pages/template/qa.rst
   _pages/template/documentation.rst
   {% if cookiecutter.docker == 'y' %}
   _pages/template/pycharm.rst
   _pages/template/docker.rst
   _pages/template/gitlab-ci.rst
   _pages/template/going-to-production.rst
   _pages/template/production.rst
   {% endif %}

Indexes and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
