FROM python:alpine

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY . ./
