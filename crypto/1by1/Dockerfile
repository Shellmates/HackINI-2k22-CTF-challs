FROM ubuntu:20.04

# Update Ubuntu image
RUN apt-get update && apt-get upgrade -y

# Setup challenge environment
RUN apt-get install -y socat python3 python3-pip --no-install-recommends
RUN python3 -m pip install pycryptodome pycryptodomex

# Add new user "ctf:ctf"
RUN useradd -m -d /home/ctf -s /bin/bash ctf
RUN echo 'ctf:ctf' | chpasswd

# Change directory to the newly created user's directory
WORKDIR /home/ctf/

EXPOSE 8000

COPY ./entrypoint.sh /home/ctf
COPY ./challenge/challenge.py /home/ctf
RUN chmod +x /home/ctf/entrypoint.sh 
RUN chmod +x /home/ctf/challenge.py

CMD ["/home/ctf/entrypoint.sh"]
