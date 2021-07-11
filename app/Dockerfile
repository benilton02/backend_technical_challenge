FROM python:3.8-alpine

WORKDIR /docker-flask-api

ADD . /docker-flask-api

RUN apk add build-base

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]