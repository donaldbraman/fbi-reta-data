FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip-3.3 install zipfile


MAINTAINER Donald Braman
