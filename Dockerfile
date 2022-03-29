FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install --system

COPY . ./