FROM python:3.7-alpine3.7

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
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true


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
     tini


# Creating folders, and files for a project:

COPY . /code
WORKDIR /code

# This is a special case. We need to run this script as entry point:
COPY ./docker/django/entrypoint.sh /docker-entrypoint.sh


# Project initialization:

RUN chmod +x "/docker-entrypoint.sh" \
  && pip install pipenv \
  && pipenv install $(test "$DJANGO_ENV" == production || echo "--dev") --deploy --system --ignore-pipfile

ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]
