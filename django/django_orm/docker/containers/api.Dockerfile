FROM python:3.8-slim

RUN apt-get update && apt-get install -y gettext

ADD . /django_orm

RUN chmod +x /django_orm/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /django_orm/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /django_orm/requirements/dev.txt
