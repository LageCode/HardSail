# HardSail

Tailored Odoo solution for TechBuild, a fictitious company specializing in custom-built PCs and hardware component sales.

## Intro

### This module handles two main services

1. Custom PC Assembly: Customers can choose individual components (CPU, GPU, RAM, etc.), and TechBuild will assemble the PC.
2. Component Sales: Customers can also purchase components individually to assemble their own PC.

### Project Objectives

- **Component Catalog**: Manage a comprehensive catalog of components with details like pricing, stock, and technical specifications, ensuring compatibility (e.g., motherboard and processor).
- **Custom PC Orders**: Enable customers to create orders for custom PCs. Odoo will automatically verify component compatibility and calculate the total price.
- **Order and Stock Management**: Track stock levels and manage orders for both custom PCs and individual components.
- **Invoicing and Payments**: Generate invoices and handle multiple payment methods (credit card, bank transfer, etc.).
- **Reporting Dashboard**: Provide insights into sales performance, stock levels, and profitability for the company.

## Getting Started

- Launch the containers: `docker compose up -d`
- Connect to *localhost:8070* and create a db, *mydb*

## Manage odoo containers

- Stop containers: `docker compose stop`
- Restart containers: `docker compose start`
- Remove containers: `docker compose down`

## Attach shell to odoo

- `docker compose exec web odoo shell -d HardSail --db_host db --db_password odbpwd`

## Transfer data

- Export data: `./export-data.sh` -> This script will export volume data from odoo db and web containers into tar files in the *backup/* directory.
- Import data: `./import-data.sh` -> This script will load the volume data from *backup/odoo-db-data.tar* and *backup/odoo-web-data.tar* to corresping volumes.
