FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

EXPOSE 8000

RUN apk add --update py-pip

RUN pip install -r requirements.txt