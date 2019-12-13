# This Dockerfile uses multi-stage build to customize DEV and PROD images:
# https://docs.docker.com/develop/develop-images/multistage-build/

FROM python:3.7.5-alpine3.9 as development_build

LABEL maintainer="{{ cookiecutter.project_name }}@{{ cookiecutter.organization }}"
LABEL vendor="{{ cookiecutter.organization }}"

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # dockerize:
  DOCKERIZE_VERSION=v0.6.1 \
  # poetry:
  POETRY_VERSION=1.0.0


# System deps:
RUN apk --no-cache add \
    bash \
    build-base \
    curl \
    gcc \
    gettext \
    git \
    libffi-dev \
    linux-headers \
    openssl \
    musl-dev \
    postgresql-dev \
    tini \
  # Installing `poetry` package manager:
  # https://github.com/sdispater/poetry
  && pip install -U "pip<19.0" \
  && pip install "poetry==$POETRY_VERSION" \
  # Installing `dockerize` utility:
  # https://github.com/jwilder/dockerize
  && wget "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && tar -C /usr/local/bin -xzvf "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && rm "dockerize-alpine-linux-amd64-${DOCKERIZE_VERSION}.tar.gz"

# Copy only requirements, to cache them in docker layer:
WORKDIR /pysetup
COPY ./poetry.lock ./pyproject.toml /pysetup/

# This is a special case. We need to run this script as an entry point:
COPY ./docker/django/entrypoint.sh /docker-entrypoint.sh

# Project initialization:
RUN chmod +x "/docker-entrypoint.sh" \
  && poetry config virtualenvs.create false \
  && poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# This dir will become the mountpoint of development code:
WORKDIR /code

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]


# The following stage is only for Prod:
# https://wemake-django-template.readthedocs.io/en/latest/pages/template/production.html

FROM development_build as production_build

COPY . /code
