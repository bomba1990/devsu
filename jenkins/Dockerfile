FROM jenkins/jenkins:lts


USER root
RUN  apt-get update && apt-get install -y python-pip
RUN pip install awscli
USER jenkins
