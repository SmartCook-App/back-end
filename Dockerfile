# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py runserver

COPY . /code/
