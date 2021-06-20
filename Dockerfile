#
# docker build -t mellow-buffalo .
#
FROM ubuntu:18.04
#
#ENV RUNTIME_ENV dev
ENV RUNTIME_ENV prod
#
RUN apt-get update && apt-get -y upgrade
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip virtualenv
RUN apt-get install -y vim
#
RUN pip3 install --upgrade pip
#
COPY . /mellow-buffalo
#
WORKDIR /mellow-buffalo
RUN pip3 install -r requirements.txt
#
ENTRYPOINT ["bin/runner.sh"]
#