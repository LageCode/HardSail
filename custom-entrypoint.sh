#!/bin/bash

set -e

# Wait for PostgreSQL to be ready
/usr/local/bin/wait-for-postgres.sh db

# Execute Odoo with any provided arguments
exec odoo "$@"