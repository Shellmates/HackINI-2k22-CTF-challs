FROM python:3-alpine

RUN apk update && \
    apk add socat libc-dev

RUN adduser --disabled-password --no-create-home ctf
RUN adduser --disabled-password --no-create-home ctf-cracked

COPY challenge /challenge/

WORKDIR /challenge

RUN chown ctf-cracked:ctf wrapper && chown ctf-cracked:ctf chall.py
RUN chmod 750 wrapper && chmod +x entrypoint.sh && chmod 400 chall.py && chmod u+s wrapper
    
ENTRYPOINT ["./entrypoint.sh"]
