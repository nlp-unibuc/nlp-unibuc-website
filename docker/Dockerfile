FROM ubuntu:16.05

MAINTAINER Sergiu Nisioi <sergiu.nisioi@fmi.unibuc.ro>

USER root

RUN apt-get update 
RUN apt-get install -y build-essential git python python-pip
RUN pip install pelican
RUN pip install typogrify

RUN mkdir /home/nlp
USER nlp
ADD . /nlp-unibuc-website
WORKDIR /nlp-unibuc-website

RUN git submodule init
RUN git submodule update
RUN git remote add deploy https://github.com/nlp-unibuc/nlp-unibuc.github.io.git
RUN git config remote.deploy.push deploy:master
