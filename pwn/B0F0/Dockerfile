FROM ubuntu:latest

RUN apt-get update &&  apt-get install socat -y && apt-get install gcc-multilib -y

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh challenge && \
    chown -R root:root .
    
EXPOSE 1337

ENTRYPOINT ["/challenge/entrypoint.sh"]