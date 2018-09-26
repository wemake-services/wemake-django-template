# {{ cookiecutter.project_name }}

{{ cookiecutter.project_verbose_name }}

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [{% gitcommit %}](https://github.com/wemake-services/wemake-django-template/tree/{% gitcommit %}). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/{% gitcommit %}...master) since then.


[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) [![build status](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/build.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master) [![coverage report](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/coverage.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master)


## Prerequisites

You will need:

- `python3.6` (see `Pipfile` for full version)
- `postgresql` with version `9.6`
- `docker` with [version at least](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix) `18.02`


## Hot start

It is highly recommended to read [documentation](https://wemake-django-template.readthedocs.io/en/latest) before starting a work. Absolute minimum to start a project, requires:

- Setting up secret [configuration](https://wemake-django-template.readthedocs.io/en/latest/_pages/template/configuration.html#configuration)
- [Running](https://wemake-django-template.readthedocs.io/en/latest/_pages/template/docker.html) a docker

If you still want to proceed, you can launch project with

```bash
docker-compose up
```

But do note that `Installing dependencies from Pipfile.lock` and `Looking in indexes: https://pypi.python.org/simple` steps can take a while. You also need to setup the `config/.env` file before running docker-compose.


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`pipenv`](https://github.com/kennethreitz/pipenv) (**required**)
- `pycharm 2017` (optional)


## Documentation

Full documentation is available here: [`docs/`](docs).
