#!/bin/bash

IMAGE_NAME=crawler

#------------Step 1. Build Image if not exists -------------------------------------------#
echo -e "\n>>>[BUILD] 1. Build Image '$IMAGE_NAME'\n"
image_exists=$(docker images -q $IMAGE_NAME)
if [ -z "$image_exists" ]; then
    docker build -t $IMAGE_NAME .
else
    echo "Image $IMAGE_NAME already exists"
    docker build -t $IMAGE_NAME . 
fi
