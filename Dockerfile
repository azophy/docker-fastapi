FROM python:3.8-alpine

LABEL maintainer="Abdurrahman Shofy Adianto <abdurrahman.shofy@gmail.com>"

WORKDIR /app
EXPOSE 80


COPY requirements.txt /app
# install dependencies required to compile python packages
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
  && pip install --no-cache-dir -r requirements.txt \
  # remove unused programes to reduce sizes
  && apk del .build-deps gcc libc-dev make

COPY . /app

CMD gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 server:app
