#!/bin/bash

CONTAINER_NAME=crawler_api
IMAGE_NAME=crawler

#------------Step 0. Stop and Remove Container if already exists and is running ----------#
container_running=$(docker ps -q -f name=$CONTAINER_NAME)
if [ -z "$container_running" ]; then
    echo -e "\n>>>[STOP] 0-1. STOP Container '$CONTAINER_NAME' \n"
    docker stop $CONTAINER_NAME
    echo -e "\n>>>[REMOVE] 0-2. Remove Container '$CONTAINER_NAME' \n"
    docker rm $CONTAINER_NAME
fi


#------------Step 1. Build Image if not exists -------------------------------------------#
echo -e "\n>>>[BUILD] 1. Build Image '$IMAGE_NAME'\n"
image_exists=$(docker images -q $IMAGE_NAME)
if [ -z "$image_exists" ]; then
    docker build -t $IMAGE_NAME .
else
    echo "Image $IMAGE_NAME already exists"
    docker build -t $IMAGE_NAME . 
fi


#------------Step 2. Run Container -------------------------------------------------------#
echo -e "\n>>>[RUN] 2. Run Container\n"
docker run --name $CONTAINER_NAME $IMAGE_NAME



