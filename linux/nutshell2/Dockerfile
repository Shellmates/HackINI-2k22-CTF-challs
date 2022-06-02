FROM ubuntu:22.04


RUN apt-get update && \
    apt-get install -y socat zsh

RUN useradd -M -s /bin/zsh nutshell2

RUN mkdir -p /challenge

COPY challenge/flag /challenge/
COPY challenge/nutshell2 /challenge/

RUN chown root:root /challenge/flag \
    && chmod 444 /challenge/flag \
    && chown root:root /challenge/nutshell2 \
    && chmod 555 /challenge/nutshell2 \ 
    && chmod 557 /challenge

EXPOSE 1337

COPY challenge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /challenge
USER nutshell2

ENTRYPOINT /entrypoint.sh
