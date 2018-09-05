FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    pip install psycopg2-binary && \
    apk --purge del .build-deps gcc python3-dev musl-dev postgresql-dev

RUN addgroup -g 1000 app && adduser -D -H -s none -u 1000 -G app app

RUN mkdir /app

ADD requirements.txt . 

RUN pip install -r requirements.txt

WORKDIR /app

CMD manage.py runserver 

