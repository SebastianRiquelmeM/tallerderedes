FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /var

RUN apt-get update -yqq
RUN apt-get install -yqq build-essential git byobu vim iptables 	\
			 python-dev python3-pip  			\
		         wireshark tshark 				\
			 libnfnetlink-dev libnetfilter-queue-dev 	

RUN pip3 install -U git+https://github.com/kti/python-netfilterqueue
RUN pip3 install polymorph

# Ejecute ip6tabless-nft para evitar errores al definir filtros con ip6tables
# [+] scr: https://github.com/husarnet/docker-example/issues/1
RUN update-alternatives --set ip6tables /usr/sbin/ip6tables-nft

VOLUME ["/var/develop"]
ENTRYPOINT ["byobu"]
