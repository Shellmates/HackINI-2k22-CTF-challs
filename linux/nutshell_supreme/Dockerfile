FROM archlinux:latest


RUN pacman -Syy && \
    yes | pacman -Su socat zsh sl


RUN useradd -m -d /home/supreme -s /bin/zsh supreme
COPY challenge/flag /home/supreme/flag
COPY challenge/nutshell_supreme /home/supreme/supreme

RUN find /home/supreme/flag -exec chown root:root {} \; && \ 
    find /home/supreme/flag -type f -exec chmod 774 {} \; && \
    find /home/supreme/flag -type d -exec chmod 775 {} \;


EXPOSE 1337

COPY challenge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /home/supreme
USER supreme
ENTRYPOINT /entrypoint.sh
