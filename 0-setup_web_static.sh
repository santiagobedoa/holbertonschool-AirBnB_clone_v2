#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# Install NGINX
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
# Creating directories
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
# Creating html for testing
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
# Creating symbilic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Grants permissions
sudo chown -R ubuntu:ubuntu /data/
# Creating alias for location in NGINX config
sudo sed -i '48i \\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restar service
sudo service nginx start
