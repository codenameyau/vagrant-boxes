# vagrant-boxes

### Getting Started
Download and install both [Vagrant](https://www.vagrantup.com/downloads.html)
and [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

### Commands
```bash
vagrant up
```

```bash
vagrant provision
```

```bash
vagrant destroy
```

```bash
vagrant halt
```

```bash
vagrant ssh
```

### Why Vagrant over Docker?
Vagrant and docker both essentially do the same thing, that is provision
an isolated development environment with the ability to quickly start and
destroy them.

*Simplicity*: For monoliths, Vagrant is great since you'll have a deal with
a much smaller subset of commands and problems than you do with docker. It's
as simple as downloading vagrant and virtualbox and running vagrant up and
vagrant ssh.


### Why Docker over Vagrant?
*Lightweight*: Docker containers however are much smaller than vagrant boxes, and mimic the
exact build used for production since they are shared and reusable post-build.

*Composability*: However, Docker is more complex to use and requires having around 5+ verbose
commands just to start using it. While it can be difficult to coordinate multiple
Docker containers on a development machine, it's the best viable solution
for coordinating micro-services and service-oriented architectures.


### Notes
- Try to always use the latest version of virtualbox.
- You may run into issues with port forwarding and virtual host versions.
- Google your solution.
