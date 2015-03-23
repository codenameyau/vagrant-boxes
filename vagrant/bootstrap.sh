#!/bin/bash

# Run as user: root (without -)
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
yum -y install postgresql-server postgresql-devel


################################################################
# SERVICES / ENVIRONMENT SETUP
################################################################

# Start Service: Memcached
systemctl start memcached.service
systemctl enable memcached.service

# Start Service: PostgreSQL
postgresql-setup initdb
systemctl start postgresql.service
systemctl enable postgresql.service

# Create Postgres superuser: vagrant
runuser -l postgres -c "createuser -s -e vagrant"
runuser -l vagrant -c "createdb"


################################################################
# BASH / ENVIRONMENT CONFIGURATION
################################################################

# Create new .bashrc
BASHRC="/home/vagrant/.bashrc"
echo "Creating "$BASHRC
echo -e ". /etc/bashrc" > $BASHRC

# Set Django environments to development
echo -e "export DJANGO_SETTINGS_MODULE=vanilla.settings.development" >> $BASHRC
echo -e "export DJANGO_DATABASE=development" >> $BASHRC

# Set the default directory
echo -e "cd /application/" >> $BASHRC


################################################################
# DJANGO APPLICATION SETUP
################################################################

# Pip requirements
cd /application/
pip install -r requirements/development.txt
