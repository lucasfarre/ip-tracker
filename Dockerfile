############################################################
# Dockerfile based on:
# https://hub.docker.com/_/python/
# https://github.com/docker-library/python/blob/master/2.7/onbuild/Dockerfile
# https://github.com/docker-library/python/issues/150
# http://stackoverflow.com/questions/35766638/how-to-pass-command-line-arguments-to-a-python-script-running-in-docker
############################################################

FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
ENTRYPOINT [ "python", "./iptracker.py" ]
