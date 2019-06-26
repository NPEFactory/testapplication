FROM python:3.6.8-alpine

RUN pip install flask

COPY app/* /

EXPOSE 80

ENTRYPOINT ["python", "/app/hello.py"]
