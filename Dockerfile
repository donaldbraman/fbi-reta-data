FROM python:3-slim

RUN apt-get install -qy python3-pip
RUN pip-3.3 install zipfile

MAINTAINER Donald Braman
