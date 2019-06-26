FROM python:3.6.8-alpine

RUN pip install flask

RUN mkdir /app
COPY app/* /app

RUN ls /app

EXPOSE 80

ENTRYPOINT ["python", "/app/hello.py"]
