FROM ubuntu:18.04

MAINTAINER Sergiu Nisioi <sergiu.nisioi@fmi.unibuc.ro>

USER root

RUN apt-get update 
RUN apt-get install -y build-essential git

RUN mkdir /home/nlp
USER nlp
ADD . /home/nlp/nlp-unibuc-website
WORKDIR /home/nlp/nlp-unibuc-website

RUN git submodule init
RUN git submodule update
RUN git remote add deploy https://github.com/nlp-unibuc/nlp-unibuc.github.io.git
RUN git config remote.deploy.push deploy:master
RUN pip3 install -r requirements.txt

# TODO...