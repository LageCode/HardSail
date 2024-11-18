#!/bin/bash

# Pull the latest changes from Git
git pull origin $(git branch --show-current)

# Restore Odoo data
docker run --rm -v odoo-web-data:/data -v $(pwd):/backup busybox tar xzf /backup/odoo-web-data.tar.gz -C /data

# Restore PostgreSQL data
docker run --rm -v odoo-db-data:/data -v $(pwd):/backup busybox tar xzf /backup/odoo-db-data.tar.gz -C /data
