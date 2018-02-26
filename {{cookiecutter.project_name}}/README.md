# {{ cookiecutter.project_name }}

{{ cookiecutter.project_verbose_name }}

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [{% gitcommit %}](https://github.com/wemake-services/wemake-django-template/tree/{% gitcommit %}). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/{% gitcommit %}...master) since then.

{%- if cookiecutter.docker == 'y' %}
[![build status](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/build.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master) [![coverage report](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/coverage.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master)
{%- endif %}


## Prerequisites

You will need:

- `python3.6` (see `.python_version` file. You can use `pyenv` or `pipenv` to manage versions)
- `postgresql` with version `9.6`
{%- if cookiecutter.docker == 'y' %}
- `docker` with version at least `17.07`
{%- endif %}


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`pipenv`](https://github.com/kennethreitz/pipenv) (**required**)
- `pycharm 2017` (optional)


## Documentation

Full documentation is available here: [`docs/`](docs).
