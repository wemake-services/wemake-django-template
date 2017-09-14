# {{ cookiecutter.project_name }}

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template).

## Prerequirements

You will need:

- `python3.6` (see `.python_version` file. You can use `pyenv` to manage versions)
- `postgresql` with version `9.6`


## Development

We use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`pipenv`](https://github.com/kennethreitz/pipenv) (**required**)
- `pycharm` (optional)
- [`pyenv`](https://github.com/pyenv/pyenv) (optional)

### Configuration

You will need to copy file `config/secret.toml.template` to `config/secret.toml`:

```bash
cp config/secret.toml.template config/secret.toml
```

And set all the required values. Basically, it is just a database connection and a secret key.

Or you can create file `server/settings/environments/local.py`:

```bash
cp server/settings/environments/local.py.template server/settings/environments/local.py
```

And specify any configuration you want. See `.template` version for reference.

### virtualenv

We are using `pipenv` for development. So, please do not use `virtualenv` or `pip` directly.

### Installing requirements

We are using `pipenv` to specify dependencies.

Firstly, install `pipenv`, it is recommended to do so with [`pipsi`](https://github.com/mitsuhiko/pipsi):

```bash
pip install pipsi
pipsi install pew
pipsi install pipenv
```

To install (or renew) existing dependencies run:

```bash
pipenv install -d
```

### Adding new dependencies

To add new dependency you will need to run `pipenv install` or `pipenv install -d` for development packages.

### Database setup

To create new development database run:

```bash
psql postgres -f sql/create_database.sql
```

Then migrate your database:

```bash
python manage.py migrate
```
