#!/bin/bash

# Run as root (without -)
sudo su

################################################################
# PACKAGE INSTALLATION
################################################################

# CentOS EPEL
yum -y install epel-release

# Development and System packages
yum -y install gcc kernel-devel make zlib-devel git

# Python packages
yum -y install python-devel python-pip

# Memcached
yum -y install memcached libmemcached-devel

# PostgreSQL
yum -y install postgresql-server postgresql-devel


################################################################
# SERVICES SETUP
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
# BASHRC / ENVIRONMENT CONFIGURATION
################################################################

# Copy custom bashrc
CUSTOM_BASHRC="/vagrant/.bashrc"
VAGRANT_BASHRC="/home/vagrant/.bashrc"
if [ -f $CUSTOM_BASHRC ]; then
  echo "Updating "$VAGRANT_BASHRC
  cat $CUSTOM_BASHRC > $VAGRANT_BASHRC
fi


################################################################
# DJANGO APPLICATION SETUP
################################################################

# Pip requirements
cd /application/
pip install -r requirements/development.txt
