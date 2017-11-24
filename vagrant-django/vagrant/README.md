# Vagrant CentOS 7

Follow these steps to setup and provision a vagrant box with **centos-7**.

1. Download and install both [Vagrant](https://www.vagrantup.com/downloads.html)
and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Open a terminal and navigate to the `vagrant/` directory.
3. Run: `vagrant up`
4. Grab a beer and enjoy the magic show.
5. The postgres superuser and database `vagrant` will be automatically created.
6. SSH into the vagrant box with: `vagrant ssh`
7. Run: `./manage.py syncdb` and `./manage.py migrate`
8. Start the Django server: `sudo python manage.py runserver 0.0.0.0:8000`


#### Notes
- Power off the vagrant box with: `vagrant halt`
- Try to use the latest version of virtualbox `>= 4.3.26`.
- Traffic from ports `8000` and `5432` are fowarded to the vagrant box.
Make sure that these ports are not in use in your personal machine.

#### It's not working!
It can be tough getting vagrant to seemlessly work the first time.

Please see [Solutions for Common Issues](https://github.com/codenameyau/django-vagrant-box/blob/master/vagrant/ISSUES.md)
