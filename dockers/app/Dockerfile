FROM python:3.7
ENV PYTHONUNBUFFERED 1
ADD requirements.txt . 
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
