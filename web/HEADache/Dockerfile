FROM python:alpine3.15

COPY app /app

WORKDIR /app

RUN pip3 install -r requirements.txt
 
EXPOSE 1337

ENTRYPOINT python app.py