FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y socat

COPY challenge /challenge

RUN chmod 700 /tmp

WORKDIR /challenge

RUN chmod +x entrypoint.sh challenge.py

EXPOSE 1337

ENTRYPOINT ["/challenge/entrypoint.sh"]
