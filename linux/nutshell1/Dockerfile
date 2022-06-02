FROM ubuntu:18.04


RUN apt-get update && \
    apt-get install -y socat zsh

RUN useradd -M -s /bin/zsh nutshell1

RUN mkdir -p /challenge

COPY challenge/flag /challenge/
COPY challenge/nutshell1 /challenge/

RUN chown root:root /challenge/flag \
    && chmod 444 /challenge/flag \
    && chown root:root /challenge/nutshell1 \
    && chmod 555 /challenge/nutshell1

EXPOSE 1337

COPY challenge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /challenge
USER nutshell1

ENTRYPOINT /entrypoint.sh
