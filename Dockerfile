FROM python:3.8.5-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 gcc g++ python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
RUN apk add netcat-openbsd
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app/