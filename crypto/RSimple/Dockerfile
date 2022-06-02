FROM python:3.10

RUN apt-get update && \
    apt-get install -y socat

RUN adduser --disabled-password --no-create-home ctf
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install gmpy2 pycryptodome

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x RSimple.py entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
