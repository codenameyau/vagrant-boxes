# vagrant-django
Vagrant box for CentOS 7 + Django-1.7 + Best practices from *Two Scoops of Django*.

### Generate Secrets Files
By default, your project will not run because it is missing these files:
`secrets.json` and `secrets.py`. These files are ignored in source control.

Generate these files with:
```
python start.py
```

You will first be prompted to rename your project.

### Setup Vagrant

Follow the [Vagrant Setup](https://github.com/codenameyau/django-vanilla/tree/master/vagrant#vagrant-centos-7)
to create and provision your Django Vagrant box.
