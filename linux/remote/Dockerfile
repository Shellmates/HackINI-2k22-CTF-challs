FROM ubuntu:latest

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server systemd rsyslog

RUN useradd -s /bin/bash ctf \
    && echo 'ctf:ctf' | chpasswd 


COPY challenge/flag.txt /

RUN chmod 444 /flag.txt 
RUN rm /usr/bin/scp

COPY challenge/sshd_config /etc/ssh/sshd_config
COPY challenge/.bashrc /etc/bash.bashrc

ENTRYPOINT service rsyslog start \
    && service ssh start \
    && tail -f --retry /var/log/auth.log
