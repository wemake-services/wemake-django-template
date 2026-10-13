# Welcome to wemake-django-template’s documentation!

What this project is all about?
The main idea of this project is to provide a fully configured
template for `django` projects, where code quality, testing,
documentation, security, and scalability are number one priorities.

This template is a result of implementing
[our processes](https://github.com/wemake-services/meta),
it should not be considered as an independent part.

## Goals

When developing this template we had several goals in mind:

- Development environment should be bootstrapped easily,
  so we use `docker-compose` for that
- Development should be consistent, so we use strict quality and style checks
- Development, testing, and production should have the same environment,
  so again we develop, test, and run our apps in `docker` containers
- Documentation and codebase are the only sources of truth

## Limitations

This project implies that:

- You are using `docker` for deployment
- You are using Gitlab and Gitlab CI
- You are not using any frontend assets in `django`,
  you store your frontend separately

## Should I choose this template?

This template is oriented on big projects,
when there are multiple people working on it for a long period of time.

If you want to simply create a working prototype without all these
limitations and workflows - feel free to choose any
[other template](https://github.com/audreyr/cookiecutter#python-django).

## How to start

You should start with reading the documentation.
Reading order is important.

There are multiple processes that you need to get familiar with:

- First time setup phase: what system requirements you must fulfill,
  how to install dependencies, how to start your project
- Active development phase: how to make changes, run tests and linters,
  write documentation, and use GitLab CI
- Production phase: deployment checklist, production configuration,
  and operations.

## Setting things up:

* [Overview](pages/template/overview.md)
* [Development](pages/template/development.md)
* [Django](pages/template/django.md)

## Quality assurance:

* [Documentation](pages/template/documentation.md)
* [Linters](pages/template/linters.md)
* [Testing](pages/template/testing.md)
* [Security](pages/template/security.md)
* [Gitlab CI](pages/template/gitlab-ci.md)

## Production:

* [Going to production](pages/template/production-checklist.md)
* [Production](pages/template/production.md)

## Extras:

* [Upgrading template](pages/template/upgrading-template.md)
* [Frequently asked questions](pages/template/faq.md)
* [Troubleshooting](pages/template/troubleshooting.md)
