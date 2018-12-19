FROM python:3.6.6-alpine3.7

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
  POETRY_VERSION=0.12.10


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

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# This is a special case. We need to run this script as an entry point:
COPY ./docker/django/entrypoint.sh /docker-entrypoint.sh

# Project initialization:
RUN chmod +x "/docker-entrypoint.sh" \
  && poetry config settings.virtualenvs.create false \
  && poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]
