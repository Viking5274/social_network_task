# syntax=docker/dockerfile:1
FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /test_proj

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
# COPY Docker/app-entrypoint.sh .

EXPOSE 8000
