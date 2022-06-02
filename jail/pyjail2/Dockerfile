FROM python:3.10

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server sudo systemd rsyslog

RUN useradd -M -s /bin/bash ctf-cracked \
    && useradd -M -s /bin/bash ctf \
    && echo 'ctf:ctf' | chpasswd \
    && usermod -aG sudo ctf

COPY challenge/flag.txt /
COPY challenge/sudoers /etc/sudoers
COPY challenge/sshd_config /etc/ssh/sshd_config
COPY challenge/chall.py /chall.py

RUN chown root:ctf-cracked /flag.txt \
    && chmod 440 /flag.txt \
    && chmod +x /chall.py 

RUN chmod 770 /tmp /var/tmp

ENTRYPOINT service rsyslog start \
    && service ssh start \
    && tail -f --retry 