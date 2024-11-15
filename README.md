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

1. `mkdir odoo`
2. `cd odoo`
3. `docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -v odoo-db-data:/var/lib/postgresql/data postgres:15`
4. `docker run -v odoo-data:/var/lib/odoo -v ./addons:/mnt/extra-addons -d -p 8069:8069 --link odoo-db:db -t --name odoo odoo:17`
