#!/bin/bash
# import-data.sh

# Check for backup files
if [ ! -f ./backup/hardsail_db.sql ] || [ ! -f ./backup/odoo_filestore.tar.gz ]; then
    echo "Error: Backup files not found in ./backup/"
    exit 1
fi

# Stop containers
echo "Stopping containers..."
docker compose down

# Start database
echo "Starting database container..."
docker compose up -d db
sleep 5  # Wait for database to be ready

# Import database
echo "Importing database..."
docker compose exec db dropdb -U odoo HardSail || true
docker compose exec db createdb -U odoo HardSail
cat ./backup/hardsail_db.sql | docker compose exec -T db psql -U odoo HardSail

# Import filestore
echo "Importing filestore..."
docker run --rm \
    -v hardsail_odoo-web-data:/data \
    -v ./backup:/backup \
    ubuntu \
    bash -c "rm -rf /data/* && tar -xzf /backup/odoo_filestore.tar.gz -C /data"

# Start all containers
echo "Starting Odoo..."
docker compose up -d

echo "Import completed! Please wait a few moments for Odoo to start."