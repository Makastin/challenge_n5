FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential libmagic-dev \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev 

# Requirements are installed here to ensure they will be cached.
COPY ./challenge_n5/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app

COPY ./challenge_n5/ .

EXPOSE 8000
