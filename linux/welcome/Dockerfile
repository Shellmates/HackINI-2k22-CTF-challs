FROM python:3.10

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server systemd rsyslog

RUN useradd -M -s /bin/bash ctf \
    && echo 'ctf:ctf' | chpasswd 

COPY challenge/sudoers /etc/sudoers
COPY challenge/sshd_config /etc/ssh/sshd_config
COPY challenge/01-custom /etc/update-motd.d/01-custom

RUN chmod +x /etc/update-motd.d/01-custom && chmod 770 /tmp /var/tmp

ENTRYPOINT service rsyslog start \
    && service ssh start \
    && tail -f --retry 