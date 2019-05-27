# This Dockerfile uses multi-stage build to customize DEV and PROD images:
# https://docs.docker.com/develop/develop-images/multistage-build/

FROM python:3.7.3-alpine3.9 as development_build

LABEL maintainer="sobolevn@wemake.services"
LABEL vendor="wemake.services"

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=0.12.15


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
     musl-dev \
     postgresql-dev \
     tini \
  && pip install "poetry==$POETRY_VERSION"

# Copy only requirements, to cache them in docker layer
WORKDIR /pysetup
COPY ./poetry.lock ./pyproject.toml /pysetup/

# This is a special case. We need to run this script as an entry point:
COPY ./docker/django/entrypoint.sh /docker-entrypoint.sh

# Project initialization:
RUN chmod +x "/docker-entrypoint.sh" \
  && poetry config settings.virtualenvs.create false \
  && poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# This dir will become the mountpoint of development code
WORKDIR /code

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]


# The following stage is only for Prod: 
# https://wemake-django-template.readthedocs.io/en/latest/pages/template/production.html

FROM development_build as production_build

COPY . /code

