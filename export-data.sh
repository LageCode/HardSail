#!/bin/bash
# export-data.sh

# Create backup directory if it doesn't exist
mkdir -p ./backup

# Make sure DB is running
echo "Ensuring database is running..."
docker compose up -d db
sleep 5  # Give DB time to start

# Export database using pg_dump with network connection
echo "Exporting HardSail database..."
docker compose exec db pg_dump -U odoo HardSail > ./backup/hardsail_db.sql

# Export filestore
echo "Exporting Odoo filestore..."
docker run --rm \
    -v hardsail_odoo-web-data:/data \
    -v ./backup:/backup \
    ubuntu \
    tar -czf /backup/odoo_filestore.tar.gz -C /data .

# Fix permissions
echo "Fixing backup file permissions..."
sudo chown $(whoami):$(whoami) ./backup ./backup/*

echo "Export completed!"