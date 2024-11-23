#!/bin/bash 
# export-data.sh

# Run the check_docker_compose.sh script 
./docker-status.sh 

# Capture the exit status 
STATUS=$?

# Check the status and perform actions accordingly 
if [ $STATUS -eq 0 ]; then 
    docker-compose stop
fi

docker run --rm -v hardsail_odoo-db-data:/data -v ./backup:/backup ubuntu tar cvf /backup/odoo-db-data.tar -o /data
docker run --rm -v hardsail_odoo-web-data:/data -v ./backup:/backup ubuntu tar cvf /backup/odoo-web-data.tar -o /data

sudo chown $(whoami):$(whoami) ./backup ./backup/*

gzip ./backup/*

git add ./backup