FROM python:3.8-slim

WORKDIR /docker-flask-api

ADD . /docker-flask-api

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]