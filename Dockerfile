FROM python:3.8-alpine

WORKDIR /app
EXPOSE 80

COPY requirements.txt /app
RUN pip install --no-cache -r requirements.txt

COPY . /app

CMD gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
