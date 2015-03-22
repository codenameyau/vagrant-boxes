# Vagrant CentOS 7

Follow these steps to setup and provision a vagrant box with **centos-7**.

1. Download and install both [Vagrant](http://www.vagrantup.com/downloads)
and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Open a terminal and navigate to this directory.
3. Run: `vagrant up`
4. Enjoy the magic show.
5. Once your box has been provisioned, you can ssh into the vagrant box with `vagrant ssh`
6. To start your Django server, run: `sudo python manage.py runserver 0.0.0.0:8000`
7. To power off the vagrant box (outside of ssh), run: `vagrant halt`
