# #!/bin/bash

# # Define variables
# GROUP_NAME="hardsail_devgroup"
# GROUP_ID=1002  # GID for the group
# USER_NAME="odoo"
# USER_ID=1001  # UID for the user (can be modified as needed)

# # Function to create group and user on the host
# create_host_group_user() {
#     # Create group if it doesn't exist
#     if ! getent group $GROUP_NAME >/dev/null; then
#         sudo groupadd -g $GROUP_ID $GROUP_NAME
#         echo "Group $GROUP_NAME created with GID $GROUP_ID on host."
#     fi

#     # Add current user to the group
#     sudo usermod -aG $GROUP_NAME $(whoami)
#     echo "User $(whoami) added to group $GROUP_NAME on host."
# }

# # Function to create group and user in Docker containers
# create_docker_group_user() {
#     local container=$1

#     # Create group in the container if it doesn't exist
#     docker exec -it --user root $container bash -c "
#         if ! getent group $GROUP_NAME >/dev/null; then
#             groupadd -g $GROUP_ID $GROUP_NAME
#             echo 'Group $GROUP_NAME created with GID $GROUP_ID in $container.'
#         fi

#         # Add user to the group if it exists
#         if id -u $USER_NAME >/dev/null 2>&1; then
#             usermod -aG $GROUP_NAME $USER_NAME
#             echo 'User $USER_NAME added to group $GROUP_NAME in $container.'
#         fi
#     "
# }

# # Function to set permissions on directories
# set_permissions() {
#     local dir=$1

#     # Change group ownership and set permissions
#     sudo chown -R :$GROUP_NAME $dir
#     sudo chmod -R 775 $dir
#     sudo chmod g+s $dir
#     echo "Permissions set for $dir."
# }

# # Main script execution
# create_host_group_user

# # Create group and user in web and db containers
# create_docker_group_user "hardsail-web-1"
# create_docker_group_user "hardsail-db-1"

# # Set permissions on all subdirectories within the addons directory
# for dir in /home/lage/Projects/hardsail/addons/*; do
#     if [ -d "$dir" ]; then
#         set_permissions "$dir"
#     fi
# done
