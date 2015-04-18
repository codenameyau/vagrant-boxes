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

Good luck. Google is your best friend. Here are some ways I've solved this issue:

#### Update your virtualbox
Try updating virtualbox to the latest version. I use version `4.3.26` on Linux Mint.

#### Reconfigure virtualbox
Run this command: `sudo dpkg-reconfigure virtualbox-4.3`

#### Re-activate Guest Additions
Inside your vagrant virtual machine run: `sudo /etc/init.d/vboxadd setup`


## Warnings
If you get the following warning:

```bash
GuestAdditions versions on your host and guest do not match.
```

Then you should install the following plugin:

`vagrant plugin install vagrant-vbguest`
