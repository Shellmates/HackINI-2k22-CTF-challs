FROM python:3.8

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server sudo systemd rsyslog

RUN useradd -s /bin/bash ctf \
    && echo 'ctf:ctf' | chpasswd \
    && usermod -aG sudo ctf

WORKDIR /challenge

COPY challenge/flag.txt /
COPY challenge/sshd_config /etc/ssh/sshd_config

EXPOSE 22

ENTRYPOINT service rsyslog start \
    && service ssh start \
    && tail -f --retry /var/log/auth.log
