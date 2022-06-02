FROM php:7.3-apache

RUN apt-get update 

COPY ./challenge/* /var/www/html/

RUN echo "\nshellmates{yOU_M4De_yOUr_waY_7hRough_iT}" >> /etc/passwd

WORKDIR /var/www/html