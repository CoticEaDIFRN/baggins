FROM python:3
ENV PYTHONUNBUFFERED 1
ADD requirements.txt . 
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app

