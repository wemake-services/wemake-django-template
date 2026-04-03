# How to contribute

This is a how-to-contribute guide for the template itself.
This guide is not about contributing to the project that is created
using this template.


## Dependencies

We use `uv` to manage the [dependencies](https://github.com/astral-sh/uv).

To install them you would need to run `sync` command:

```bash
uv sync
```

To activate your `virtualenv` run `. .venv/bin/activate`.


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


## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
