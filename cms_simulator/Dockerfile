FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN apt-get install curl -y

WORKDIR /

COPY cms /cms
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install

COPY .env .env

EXPOSE 9090

ENTRYPOINT ["pipenv", "run", "cms"]
