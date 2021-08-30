FROM ubuntu:20.04


RUN apt-get update
RUN apt-get upgrade -y
WORKDIR /usr/local/
RUN mkdir -p /app


# WORKDIR ./app
COPY ./app/data ./app/data
COPY ./app/run_dash_app.py ./app
COPY ./app/plotly_layout.py ./app
COPY ./app/requirements.txt ./app


# RUN apt-get install -y python3 python-setuptools python3-pip
RUN apt-get update
RUN apt-get -y install python3-pip
# RUN pip3 install --upgrade pip
RUN pip3 install -r ./app/requirements.txt

# Set standard Python ENV
ENV PYTHONUNBUFFERED 1 # ensures that python output is sent straight to the terminal

CMD python3 ./app/run_dash_app.py

# docker remove all README_images
# docker rm -f $(docker README_images -a -q)
# docker rmi -f $(docker README_images -a -q)


# docker stop all running containers
# docker stop $(docker ps -a -q)

# docker remove all containers
# docker rm $(docker README_images -a -q)

# enter my docker container
# docker exec -it myapp_container /bin/bash

