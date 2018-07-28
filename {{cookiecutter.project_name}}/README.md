# {{ cookiecutter.project_name }}

{{ cookiecutter.project_verbose_name }}

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [{% gitcommit %}](https://github.com/wemake-services/wemake-django-template/tree/{% gitcommit %}). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/{% gitcommit %}...master) since then.


[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](http://wemake.services) [![build status](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/build.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master) [![coverage report](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/coverage.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master)


## Prerequisites

You will need:

- `python3.6` (see `Pipfile` for full version)
- `postgresql` with version `9.6`
- `docker` with [version at least](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix) `18.02`


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`pipenv`](https://github.com/kennethreitz/pipenv) (**required**)
- `pycharm 2017` (optional)


## Documentation

Full documentation is available here: [`docs/`](docs).
