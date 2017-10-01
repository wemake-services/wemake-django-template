FROM python:3.6.2-alpine

LABEL maintainer="sobolevn@wemake.services"

ENV PIPENV_SHELL_COMPAT=true PIPENV_COLORBLIND=true PIPENV_NOSPIN=true


# System deps:

RUN apk update \
    && apk --no-cache add musl-dev postgresql-dev gcc git curl \
    && apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/main python3-dev


# Creating folders, and files for a project:

RUN mkdir /code
WORKDIR /code

ADD . /code


# Project initialization:

RUN pip install pipenv \
  && test "$DJANGO_ENV" == development && echo "dev"; pipenv install --dev --deploy --system || echo "prod"; pipenv install --system --deploy


# Creating users and groups:

RUN addgroup -S django \
  && adduser -S -g django django \
  && chown -R django:django /code \
  && chmod +x /code/docker/django/entrypoint.sh \
  && chmod +x /code/docker/django/wait-for-command.sh
USER django

ENTRYPOINT ["sh", "/code/docker/django/entrypoint.sh"]
