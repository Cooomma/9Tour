FROM python:3.6.5-alpine3.6
MAINTAINER @Cooomma

COPY . /app

RUN pip install -U pip
RUN pip install -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT python /app/main.py
