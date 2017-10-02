# wemake-django-template

[![wemake.services](https://img.shields.io/badge/style-wemake.services-green.svg?label=&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](http://wemake.services) [![Build Status](https://travis-ci.org/wemake-services/wemake-django-template.svg?branch=master)](https://travis-ci.org/wemake-services/wemake-django-template) [![Documentation Status](https://readthedocs.org/projects/wemake-django-template/badge/?version=latest)](http://wemake-django-template.readthedocs.io/en/latest/?badge=latest)


Bleeding edge `django` template focused on code quality and security.

---

## Features

- [`pipenv`](https://docs.pipenv.org/) for managing dependencies
- `pytest` and `flake8` for testing and linting
- [`pre-commit`](http://pre-commit.com/) hooks for consistent development
- `docker-compose` for development and production
- `sphinx` for documentation
- `Gitlab CI` with full pipeline (`build`, `test`, and `deploy`) configured by default
- [`Caddy`](https://caddyserver.com/) with [`https`](https://caddyserver.com/docs/automatic-https) and `http/2` turned on by default


## Requirements

You will need:

- `python3`
- [`cookiecutter`](http://cookiecutter.readthedocs.io/)


## Installation

```bash
cookiecutter gh:wemake-services/wemake-django-template
```


## License

MIT.
