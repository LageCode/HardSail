#!/bin/bash

# update-module.sh
MODULE_NAME=$1
DATABASE=${2:-HardSail}  # Default to HardSail if no database specified

if [ -z "$MODULE_NAME" ]
then
    echo "Usage: ./update-module.sh <module_name> [database_name]"
    exit 1
fi

docker-compose run --rm web odoo -u "$MODULE_NAME" -d "$DATABASE" --stop-after-init