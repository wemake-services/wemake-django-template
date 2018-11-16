# wemake-django-template

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) [![Build Status](https://travis-ci.org/wemake-services/wemake-django-template.svg?branch=master)](https://travis-ci.org/wemake-services/wemake-django-template) [![Documentation Status](https://readthedocs.org/projects/wemake-django-template/badge/?version=latest)](http://wemake-django-template.readthedocs.io/en/latest/?badge=latest) [![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/wemake-services/wemake-django-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)


Bleeding edge `django` template focused on code quality and security.

---

## Purpose

This project is used to scaffold a `django` project structure. Just like `django-admin.py startproject` but better.


## Features

- Always [`up-to-date`](https://github.com/wemake-services/wemake-django-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) with the help of [`@dependabot`](https://dependabot.com/)
- [`pipenv`](https://docs.pipenv.org/) for managing dependencies
- [`mypy`](https://mypy.readthedocs.io) for optional static typing
- `pytest`, `pylint`, and `flake8` for testing and linting
- [`pre-commit`](https://pre-commit.com/) hooks for consistent development
- `docker` for development, testing, and production
- [`sphinx`](http://www.sphinx-doc.org/en/master/) for documentation
- [`Gitlab CI`](https://about.gitlab.com/gitlab-ci/) with full `build`, `test`, and `deploy` pipeline configured by default
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


## Who are using this template?

If you use our template, please add yourself or your company [in the list](https://github.com/wemake-services/wemake-django-template/wiki/Who-is-using-this-template).

We offer free email support for anyone who is using this.
If you have any problems or questions, drop us a line at [`contact@wemake.services`](mailto:contact@wemake.services).
And we will try to help you.


## License

MIT. See [LICENSE.md](https://github.com/wemake-services/wemake-django-template/blob/master/LICENSE.md) for more details.
