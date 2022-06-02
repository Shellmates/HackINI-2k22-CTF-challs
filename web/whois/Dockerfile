FROM php:7.3-apache

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install whois netbase

COPY challenge/ /var/www/html/

COPY flag.txt /var/www/html/

WORKDIR /var/www/html

RUN chown -R root:root /var/www/html
RUN chmod 444 flag.txt