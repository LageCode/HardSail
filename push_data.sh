#!/bin/bash

# Backup Odoo data
docker run --rm -v odoo-web-data:/data -v $(pwd):/backup busybox tar czf /backup/odoo-web-data.tar.gz -C /data .

# Backup PostgreSQL data
docker run --rm -v odoo-db-data:/data -v $(pwd):/backup busybox tar czf /backup/odoo-db-data.tar.gz -C /data .

# Add backups to Git
git add odoo-web-data.tar.gz odoo-db-data.tar.gz
git commit -m "Backup Odoo and PostgreSQL data"
git push origin master
