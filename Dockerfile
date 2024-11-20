FROM odoo:17

# Install locales and ensure the system uses UTF-8
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# Copy custom scripts
COPY wait-for-postgres.sh /usr/local/bin/wait-for-postgres.sh
COPY custom-entrypoint.sh /usr/local/bin/custom-entrypoint.sh
RUN chmod +x /usr/local/bin/wait-for-postgres.sh /usr/local/bin/custom-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/custom-entrypoint.sh"]