# How to contribute

This is a how-to-contribute guide for the template itself.
This guide is not about contributing to the project that is created
using this template.

## Dependencies

We use `poetry` to manage the [dependencies](https://github.com/python-poetry/poetry).

To install them you would need to run `install` command:

```bash
poetry install
```

To activate your `virtualenv` run `poetry shell`.


## Linting

We use `flake8` to run linting.
We use `wemake-python-styleguide` as the main code style rules.
Run:

```bash
flake8 .
```


## Unit tests

We use `pytest` to run unit tests. Run:

```bash
pytest
```


## Integration tests

We use `docker` to run integration tests.
Make sure it is up and running. Then run:

```bash
sh tests/test_integration.sh
```


## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
