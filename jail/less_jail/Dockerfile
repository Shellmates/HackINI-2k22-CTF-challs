FROM ubuntu:18.04   

RUN apt-get update && \
    apt-get install -y openssh-server sudo less


RUN useradd -m -s /bin/bash ch1
RUN echo 'ch1:ch1' | chpasswd

COPY challenge/real_flag /home/ch1/real_flag
COPY challenge/fakeflag /home/ch1/fakeflag
COPY challenge/my_less /home/ch1/my_less
COPY challenge/perms /etc/sudoers

RUN echo "./my_less\nkill -9  \$(ps | grep bash | awk '{print $1}')" >/home/ch1/.bashrc

RUN chown  root:root /home/ch1/real_flag /home/ch1/.bashrc /home/ch1/fakeflag /home/ch1/my_less

RUN chmod 700 /tmp

WORKDIR /challenge

EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null
