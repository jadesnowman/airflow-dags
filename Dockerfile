FROM python:3.9.19-slim

COPY . /app

RUN pip install -r /app/requirements.txt