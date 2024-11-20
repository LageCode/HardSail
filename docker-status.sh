#!/bin/bash 

# Path to your docker-compose file 
COMPOSE_FILE_PATH="./docker-compose.yml" 

# Check if any service is running 
if [ "$(docker-compose -f $COMPOSE_FILE_PATH ps -q)" ]; then 
    echo "Docker Compose services are running." 
    exit 0
else 
    echo "No Docker Compose services are running."
    exit 1 
fi