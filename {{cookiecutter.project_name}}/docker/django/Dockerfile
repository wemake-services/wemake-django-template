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
  PATH="/root/.poetry/bin:$PATH" \
  POETRY_VERSION=0.12.8


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
  && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/${POETRY_VERSION}/get-poetry.py | python


# Creating folders, and files for a project:
COPY . /code
WORKDIR /code

# This is a special case. We need to run this script as an entry point:
COPY ./docker/django/entrypoint.sh /docker-entrypoint.sh

# Project initialization:
RUN chmod +x "/docker-entrypoint.sh" \
  && poetry config settings.virtualenvs.create false \
  && poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]
