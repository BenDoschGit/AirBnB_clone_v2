#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
# Check if service exists
service="nginx"
if [ ! -f "/etc/init.d/$service" ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
# Check if directories exists
DIRS=(
    "/data"
    "/data/web_static"
    "/data/web_static/releases"
    "/data/web_static/shared"
    "/data/web_static/releases/test"
)
for DIR in "${DIRS[@]}"; do
    if [ ! -d "$DIR" ]; then
        sudo mkdir -p "$DIR"
    fi
done
# Check if file exists
FILE="/data/web_static/releases/test/index.html"
if [ ! -f "$FILE" ]; then
    sudo touch "$FILE"
fi
# Add content to file
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$content" | sudo tee /data/web_static/releases/test/index.html
# Check if link exists and remove it
LINK="/data/web_static/current"
LINK_TARGET="/data/web_static/releases/test/"
if [ -e "$LINK" ]; then
    sudo rm "$LINK"
fi
# Create Link
sudo ln -s "$LINK_TARGET" "$LINK"
# Recusrively change owener and group to Ubuntu
sudo chown -R ubuntu:ubuntu /data
# Configure Nginx
sudo sed -ie "s|server_name _;|server_name bendosch.tech;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t}\n|" /etc/nginx/sites-enabled/default
