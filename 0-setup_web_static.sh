#!/usr/bin/env bash

# If Nginx is not installed, install it
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install -y nginx
    service nginx start
fi

# Create these folders
mkdir -p /data/web_static/{releases/test,shared}

# Create a HTML file
echo "<html>
    <head>
    </head>
    <body>The best school is ALX</body>
    </html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
src_file="/data/web_static/current"
dest_file="/data/web_static/releases/test/"
ln -sf "$dest_file" "$src_file"

# Give ownership of the /data/ folder to the ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_config_block="
    location /hbnb_static/ {
        alias $src_file/;
        autoindex off;
    }
"
if ! grep -q "location /hbnb_static/" "$nginx_config"; then
    sed -i "71i $nginx_config_block" "$nginx_config"
fi

# Restart Nginx
service nginx restart
