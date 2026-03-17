# {{ cookiecutter.project_name }}

{{ cookiecutter.project_verbose_name }}

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [{% gitcommit short=True %}](https://github.com/wemake-services/wemake-django-template/tree/{% gitcommit %}). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/{% gitcommit %}...master) since then.


[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake-services.github.io)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Modern REST](https://img.shields.io/badge/Modern%20REST-0C4B33?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4MCIgaGVpZ2h0PSIxMDgwIiB2aWV3Qm94PSIwIDAgMTA4MCAxMDgwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMiA3MDQuMDJMMTQ1LjQ1OSA0NjYuMTlMMjc3Ljg4MyA3MDQuMDJMMTQ1LjQ1OSA5NDEuODQ5TDIgNzA0LjAyWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTE0NS40NTkgOTQxLjg0OUwyIDcwNC4wMkgyNzcuODgzTDE0NS40NTkgOTQxLjg0OVoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik02NzguOTQ4IDcwNC4wMzVMMzQxLjIzIDEzOEwyMjcuMDcxIDMyOC4yNjRMNDM2LjM2MiA3MDQuMDM1TDMwMy4xNzcgOTQxLjg2NEg1MzYuMjVMNjc4Ljk0OCA3MDQuMDM1WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTY3OC45MzcgNzA0LjAyNkg0MzYuMzVMMzAzLjE2NiA5NDEuODU2SDUzNi4yMzlMNjc4LjkzNyA3MDQuMDI2WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTEwNzguMTcgNzA0LjAzNUw3NDAuNDUxIDEzOEw2MjYuMjkzIDMyOC4yNjRMODM1LjU4MyA3MDQuMDM1TDcwMi4zOTkgOTQxLjg2NEg5MzUuNDcyTDEwNzguMTcgNzA0LjAzNVoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0xMDc4LjE3IDcwNC4wMzVIODM1LjU4M0w3MDIuMzk5IDk0MS44NjRIOTM1LjQ3MkwxMDc4LjE3IDcwNC4wMzVaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K&color=35544A)](https://github.com/wemake-services/django-modern-rest)


## Prerequisites

You will need:

- `python3.13` (see `pyproject.toml` for exact version), use `pyenv install`
- `postgresql` (see `docker-compose.yml` for exact version)
- Latest `docker`


## Development

When developing locally, we use:

- [`poetry`](https://github.com/python-poetry/poetry) (**required**)
- [`pyenv`](https://github.com/pyenv/pyenv)


## Documentation

Full documentation is available here: [`docs/`](docs).
