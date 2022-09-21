#!/bin/bash

echo "criando o servidor..."
apt-get update
apt-get upgrade -y
apt-get install nginx -y
apt-get install unzip -y
systemctl enable nginx
systemctl start nginx

echo "Baixando e copiando os arquivos da aplicação..."
cd /tmp
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
unzip main.zip
cd linux-site-dio-main
cp -R * /var/www/html/