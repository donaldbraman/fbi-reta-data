FROM ubuntu:latest
MAINTAINER Donald Braman

RUN apt-get update
RUN apt-get install -y python3-pip
ADD .

