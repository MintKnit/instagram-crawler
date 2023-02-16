#!/bin/bash

IMAGE_NAME=crawler
USER=ampersandor

docker login

#------------Step 1. Build Image if not exists -------------------------------------------#
echo -e "\n>>>[BUILD] 1. Build Image '$IMAGE_NAME'\n"
image_exists=$(docker images -q $IMAGE_NAME)
if [ -z "$image_exists" ]; then
    docker build -t $IMAGE_NAME .
else
    echo "Image $IMAGE_NAME already exists"
    docker build -t $IMAGE_NAME . 
fi

docker tag $IMAGE_NAME docker.io/$USER/$IMAGE_NAME:latest
docker push docker.io/$USER/$IMAGE_NAME:latest

