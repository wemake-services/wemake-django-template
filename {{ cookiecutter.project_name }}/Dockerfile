FROM python:3.6.2-alpine

MAINTAINER sobolevn@wemake.services

ENV PIPENV_SHELL_COMPAT=true PIPENV_COLORBLIND=true PIPENV_NOSPIN=true


# System deps:

RUN apk update \
    && apk --no-cache add musl-dev postgresql-dev gcc git && \
    apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/main python3-dev


# Project initialization:

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install pipenv && pipenv install --system
