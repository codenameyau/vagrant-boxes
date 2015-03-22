#!/bin/bash

# Provision as root (do not use: -)
sudo su

################################################################
# PACKAGE INSTALLATION
################################################################

# Update existing packages
yum -y update

# Upgrade security packages
yum -y --security upgrade

# CentOS EPEL
yum -y install epel-release

# System packages
yum -y install gcc kernel-devel make zlib-devel

# Developer packages
yum -y install git

# Python packages
yum -y install python-devel python-pip

# Memcached
yum -y install memcached libmemcached-devel

# PostgreSQL
yum -y install postgresql-server

# Pip requirements
cd /application/
pip install -r requirements/development.txt


################################################################
# SERVICES / ENVIRONMENT SETUP
################################################################

# Start Service: Memcached
systemctl start memcached.service
systemctl enable memcached.service

# Start Service: PostgreSQL
postgresql-setup initdb
systemctl enable postgresql.service


################################################################
# BASHRC / ALIAS CUSTOMIZATION
################################################################

# Get bashrc of vagrant user
BASHRC='/home/vagrant/.bashrc'
echo "Configuring "$BASHRC
echo -e "\n#Vagrant customizations" >> $BASHRC

# Set DJANGO_SETTINGS_MODULE to development
echo -e "export DJANGO_SETTINGS_MODULE=vanilla.settings.development" >> $BASHRC

# Set default directory
echo -e "cd /application/" >> $BASHRC
