FROM python:3.6.8-alpine

RUN pip install flask

RUN mkdir /app
COPY app/* /app

RUN ls /app

EXPOSE 80

HEALTHCHECK --interval=5m --timeout=5s CMD curl -f http://localhost:80/ || exit 1

ENTRYPOINT ["python", "/app/hello.py"]
