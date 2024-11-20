#!/bin/bash

source .env

if [ "$(docker ps -q -f name=$DB_CONTAINER)" ]; then 
    echo "Shutting down $DB_CONTAINER before data export."  
fi

docker run --rm -v hardsail_odoo-db-data:/data -v ./backup:/backup ubuntu tar cvf /backup/odoo-db-data.tar /data
docker run --rm -v hardsail_odoo-web-data:/data -v ./backup:/backup ubuntu tar cvf /backup/odoo-web-data.tar /data

