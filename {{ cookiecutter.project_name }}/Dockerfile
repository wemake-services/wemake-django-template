FROM python:3.6.2-alpine

MAINTAINER sobolevn@wemake.services


# System deps:

RUN apk update \
    && apk --no-cache add musl-dev postgresql-dev gcc && \
    apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/main python3-dev


# Project initialization:

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install pipenv && pipenv install --system
