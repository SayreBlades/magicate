FROM python:3.6.1-alpine

RUN pip install slackclient
COPY app.py app.py

CMD python app.py
