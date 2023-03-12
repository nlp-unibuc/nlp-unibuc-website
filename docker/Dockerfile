FROM ubuntu:22.04


RUN apt-get update && apt-get install -y  python3 python3-pip make git

# RUN git clone --recurse-submodules https://github.com/nlp-unibuc/nlp-unibuc-website.git
COPY . /nlp-unibuc-website

WORKDIR /nlp-unibuc-website

RUN pip install -r requirements.txt

RUN make html
