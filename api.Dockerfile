# pull official base image
FROM python:3.11

# author name
LABEL author="ak4m410x01"

# set work directory
WORKDIR /app

# set default shell
SHELL [ "/bin/bash", "-c" ]

# update/upgrade container & install git
RUN apt update -qqq && \
    apt upgrade -y -qqq

# copy code files into container
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose port
EXPOSE 80
