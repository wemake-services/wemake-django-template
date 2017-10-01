# test

Test project

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template).

[![build status](https://gitlab.com/wemake.services/test/badges/master/build.svg)](https://gitlab.com/wemake.services/test/commits/master) [![coverage report](https://gitlab.com/wemake.services/test/badges/master/coverage.svg)](https://gitlab.com/wemake.services/test/commits/master)


## Prerequirements

You will need:

- `python3.6` (see `.python_version` file. You can use `pyenv` to manage versions)
- `postgresql` with version `9.6`
- `docker` with version at least `17.07`


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`pipenv`](https://github.com/kennethreitz/pipenv) (**required**)
- `pycharm` (optional)

### Configuring pre-commit hooks

We are using several pre-commit hooks to make sure everything works just fine.
To setup hooks after installing all the dependencies run:

```bash
pre-commit install
```

You will now see the test results before any commit, hooks we are using:

- [`gitlint`](http://jorisroovers.github.io/gitlint/)
- `pytest`
- [`safety`](https://github.com/pyupio/safety)

### Database setup

To create new development database run:

```bash
psql postgres -f sql/create_database.sql
```

Then migrate your database:

```bash
python manage.py migrate
```
