# Vagrant CentOS 7

Follow these steps to setup and provision a vagrant box with **centos-7**.

1. Download and install both [Vagrant](http://www.vagrantup.com/downloads)
and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Open a terminal and navigate to this directory.
3. Run: `vagrant up`
4. Grab a beer and enjoy the magic show.
5. The postgres superuser and database `vagrant` will be automatically created.
6. SSH into the vagrant box with `vagrant ssh`
7. Run: `./manage.py syncdb`
8. Start the Django server: `sudo python manage.py runserver 0.0.0.0:8000`


#### Notes
- To power off the vagrant box (outside of ssh), run: `vagrant halt`
- Your virtualbox should be at least version `4.3.26`.
You can check which version you have with `vboxmanage --version`.
- Traffic from ports `8000` and `5432` are fowarded to the vagrant box.
Make sure that these ports are not in use in your personal machine.


#### Errors
If you get the following error:

`/sbin/mount.vboxsf: mounting failed with the error: No such device`

Then you'll need to update your virtualbox to at least version `4.3.26`.

#### Warnings
If you get the following warning:

`GuestAdditions versions on your host and guest do not match.`

Then you should install the following plugin:

`vagrant plugin install vagrant-vbguest`
