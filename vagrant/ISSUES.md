# Common Vagrant and Virtualbox Issues

## Errors
If you get the following error:

```bash
Failed to mount folders in Linux guest. This is usually because
the "vboxsf" file system is not available. Please verify that
the guest additions are properly installed in the guest and
can work properly. The command attempted was:

mount -t vboxsf -o uid=`id -u vagrant`,gid=`getent group vagrant | cut -d: -f3` vagrant /vagrant
mount -t vboxsf -o uid=`id -u vagrant`,gid=`id -g vagrant` vagrant /vagrant

The error output from the last command was:

/sbin/mount.vboxsf: mounting failed with the error: No such device
```

Good luck. Google is your best friend. http://askubuntu.com/a/22745

Here are some ways I've solved this issue:

#### Update Your Virtualbox
Try updating virtualbox to the latest version. I use version `4.3.26` on Linux Mint.
Even better try to keep the guest additions in sync between your host machine
and your virtual machine.

#### Reconfigure guest additions on VM
Run this command if your vbguest fails to mount on a reboot
after a kernel update in the guest machine, i.e. `yum update`.

If you do update your kernel, run:

```bash
vagrant ssh
sudo /etc/init.d/vboxadd setup
```

Exit SSH and run:

```bash
vagrant reload
```

#### Reconfigure Virtualbox on Host
Perhaps it's your host machine that is the cause of the problem. Try installing
dkms and reconfiguring virtualbox.

```bash
sudo apt-get install dmks
sudo dpkg-reconfigure virtualbox-4.3
```

#### Install the vbguest plugin
This plugin will automatically sync you guests additions for a successfully provisioned
machine. Don't use this plugin if your machine has not been provisioned yet.

```bash
vagrant plugin install vagrant-vbguest
```
