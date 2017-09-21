# {{ cookiecutter.project_name }}

{{ cookiecutter.project_verbose_name }}

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template).

{% if cookiecutter.gitlab_ci == 'y' %}[![build status](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/build.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master) [![coverage report](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/badges/master/coverage.svg)](https://gitlab.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/commits/master){% endif %}


## Prerequirements

You will need:

- `python3.6` (see `.python_version` file. You can use `pyenv` to manage versions)
- `postgresql` with version `9.6`
{% if cookiecutter.docker == 'y' %}- `docker` with version at least `17.07`


## Docker

You can run development server locally or inside `docker` container.

To start development server inside `docker` you will need to run:

```bash
docker-compose build
docker-compose run web python manage.py migrate # and any other commands you need
docker-compose up
```

It is recommended for quickstarting the development process.{% endif %}


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`pipenv`](https://github.com/kennethreitz/pipenv) (**required**)
- `pycharm` (optional)
- [`pyenv`](https://github.com/pyenv/pyenv) (optional)

### Configuration

You will need to copy file `config/secret.env.template` to `config/secret.env`:

```bash
cp config/secret.env.template config/secret.env
```

And set all the required values. Basically, it is just a database connection and a secret key.

Or you can create file `server/settings/environments/local.py`:

```bash
cp server/settings/environments/local.py.template server/settings/environments/local.py
```

And specify any configuration you want. See `.template` version for reference.

### python, virtualenv and dependencies

We are using `pyenv` to specify interpreter version and `pipenv` to specify dependencies. So, please do not use `virtualenv` or `pip` directly.

<!-- Firstly, check that `.python-version` matches with your system `python`. If not, install new one:

```bash
pyenv install
``` -->

Then, install `pipenv`, it is recommended to do so with [`pipsi`](https://github.com/mitsuhiko/pipsi):

```bash
pip install pipsi
pipsi install pew
pipsi install pipenv
```

To install (or renew) existing dependencies run:

```bash
pipenv --three install -d
```

And to activate `virtualenv` run:

```bash
pipenv shell
```

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

### Adding new dependencies

To add new dependency you will need to run `pipenv install` or `pipenv install -d` for development packages. Make sure you specify correct `python` version.

### Database setup

To create new development database run:

```bash
psql postgres -f sql/create_database.sql
```

Then migrate your database:

```bash
python manage.py migrate
```
