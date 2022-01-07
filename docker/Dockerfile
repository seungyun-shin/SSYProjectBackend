FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

ENV APT_PACKAGES wget curl apt-transport-https ca-certificates

WORKDIR /tmp

RUN apt-get update -y&& \
    apt-get upgrade -y&& \
    apt update -y&& \
    apt upgrade -y 

RUN apt install -y git

WORKDIR /root