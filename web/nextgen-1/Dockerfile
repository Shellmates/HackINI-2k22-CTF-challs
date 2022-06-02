FROM ubuntu:latest

RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -y \
        vim curl \
        apache2 libapache2-mod-wsgi-py3 \
        python3 python3-pip

RUN pip3 install flask

# TO-DO : use mod_wsgi from source code

COPY challenge/apps/ /var/www/

COPY challenge/requirements.txt /var/www/
RUN pip install -r /var/www/requirements.txt

COPY challenge/wsgi-apps.conf /etc/apache2/sites-available/
RUN a2ensite wsgi-apps && a2dissite 000-default

COPY challenge/flag.txt /flag.txt
RUN chmod 644 /flag.txt

CMD echo "127.0.0.1 hr.dep.nextgen.org acc.dep.nextgen.org">>/etc/hosts && apachectl -D FOREGROUND
