FROM python:3.6.4-alpine3.7

LABEL maintainer="sobolevn@wemake.services"

ARG DJANGO_ENV=production
ENV PYTHONFAULTHANDLER=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_SHELL_COMPAT=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true


# System deps:

RUN apk update \
    && apk --no-cache add musl-dev postgresql-dev gcc \
      git curl bash build-base gettext linux-headers \
    && mkdir /code


# Creating folders, and files for a project:

WORKDIR /code
ADD . /code


# Project initialization:

RUN pip install pipenv && test "$DJANGO_ENV" == production && pipenv install --system --deploy || pipenv install --dev --system --deploy

ENTRYPOINT ["sh", "/code/docker/django/entrypoint.sh"]
