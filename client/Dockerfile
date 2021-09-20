FROM ubuntu:20.04
MAINTAINER sebastian.riquelme1@mail.udp.cl

EXPOSE 20 21

RUN apt-get update \
&& apt-get install -yqq lftp \
&& apt-get -yqq autoclean

CMD ["lftp", "usuario:usuario@172.17.0.2"]
