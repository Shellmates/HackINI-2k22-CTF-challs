FROM python:3.9

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        locales locales-all \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/

RUN python -m pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

WORKDIR /challenge

COPY challenge/server.py .
COPY challenge/entrypoint.sh .
COPY challenge/flag.runme .

RUN chmod +x server.py entrypoint.sh && \
    chmod 111 flag.runme

EXPOSE 8765

USER nobody

ENTRYPOINT ["./entrypoint.sh"]
