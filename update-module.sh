#!/bin/bash

# update-module.sh
MODULE_NAME=${1:-hardsail}  # Default to hardsail if no module specified
DATABASE=${2:-hardsail}  # Default to hardsail if no database specified

if [ -z "$MODULE_NAME" ]
then
    echo "Usage: ./update-module.sh <module_name> [database_name]"
    exit 1
fi

docker-compose run --rm web odoo -u "$MODULE_NAME" -d "$DATABASE" --stop-after-init
docker-compose restart web