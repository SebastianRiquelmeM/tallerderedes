FROM ubuntu:20.04
MAINTAINER sebastian.riquelme1@mail.udp.cl

EXPOSE 20 21

WORKDIR /server

ARG DEBIAN_FRONTEND=noninteractive

RUN useradd usuario
RUN echo "usuario:usuario" | chpasswd
RUN mkdir serverftp
RUN chmod -R 777 serverftp

RUN apt-get -yqq update \
&& apt-get -yqq install proftpd \
&& apt-get -yqq autoclean

RUN cd /etc/proftpd/ \
&& rm -f proftpd.conf

COPY proftpd.conf /etc/proftpd/proftpd.conf
COPY hola.txt /server/serverftp/

CMD proftpd && tail -f /dev/null
