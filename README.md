# wemake-django-template

[![wemake.services](https://img.shields.io/badge/style-wemake.services-green.svg?label=&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](http://wemake.services) [![Build Status](https://travis-ci.org/wemake-services/wemake-django-template.svg?branch=master)](https://travis-ci.org/wemake-services/wemake-django-template) [![Documentation Status](https://readthedocs.org/projects/wemake-django-template/badge/?version=latest)](http://wemake-django-template.readthedocs.io/en/latest/?badge=latest)


Bleeding edge `django` template focused on code quality and security.

---

## Purpose

This project is used to scaffold a `django` project structure. Just like `django-admin.py startproject` but better.


## Features

- Always up-to-date with the help of [`@dependabot`](https://github.com/wemake-services/wemake-vue-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
- [`pipenv`](https://docs.pipenv.org/) for managing dependencies
- [`mypy`](mypy.readthedocs.io) for optional static typing
- `pytest`, `pylint`, and `flake8` for testing and linting
- [`pre-commit`](http://pre-commit.com/) hooks for consistent development
- `docker-compose` for development, testing, and production
- `pycharm` with pre-configured local `docker` development targets
- `sphinx` for documentation
- `Gitlab CI` with full `build`, `test`, and `deploy` pipeline configured by default
- [`Caddy`](https://caddyserver.com/) with [`https`](https://caddyserver.com/docs/automatic-https) and `http/2` turned on by default


## Installation

Firstly, you will need to install dependencies:

```bash
pip install cookiecutter jinja2-git
```

Then, create a project itself:

```bash
cookiecutter gh:wemake-services/wemake-django-template
```


## License

MIT. See [LICENSE.md](https://github.com/wemake-services/wemake-django-template/blob/master/LICENSE.md) for more details.
