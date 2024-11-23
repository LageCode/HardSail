#!/bin/bash
# import-data.sh

source .env

gunzip ./backup/*

docker run --rm -v hardsail_odoo-db-data:/data -v ./backup:/backup ubuntu tar xvf /backup/odoo-db-data.tar -C /
docker run --rm -v hardsail_odoo-web-data:/data -v ./backup:/backup ubuntu tar xvf /backup/odoo-web-data.tar -C /

