What this project is all about?
The main idea of this project is to provide a fully configured template for ``django`` projects, where code quality, testing, documentation, security, and scalability are number one priorities.

This template is a result of implementing `our processes <https://github.com/wemake-services/meta>`_, it should not be considered as an independent part.


Goals
-----

When developing this template we had several goals in mind:

- Development environment should be bootstrapped easily, so we used `docker-compose` for that
- Development should be consistent, so we use strict style checks
- You should not push broken code to the repo, so we used ``pre-commit`` hooks for that
- Development, testing, and production should have the same environment, so again we are developing, testing, and running our code in ``docker`` containers
- Documentation and the codebase are the only sources of truth


Limitations
-----------

This project implies that:

- You are using ``docker`` for deployment
- You are using Gitlab CI
- You are not using any frontend assets in ``django``, you store your frontend separately


Should I choose this template?
------------------------------

This template is oriented on big projects, when there are multiple people working on it for a long period of time.

If you want to simply create a working prototype without all these limitations and workflows - feel free to choose any `other templates <https://github.com/audreyr/cookiecutter#python-django>`_.


How to start
------------

This project is created to be well documented.
You should start with reading it. It is available `online <http://wemake-django-template.readthedocs.io/en/latest>`_.
Reading order is important.

To sum up all the steps, you will have to:

1. Install dependencies
2. Configure a project and IDE
3. Run and test it
4. Know how to make changes
5. Commit your code and receive a feedback
