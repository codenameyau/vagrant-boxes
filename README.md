# django-vagrant-box
Django-1.7 + Vagrant + Best practices from *Two Scoops of Django*.

Guaranteed to save a week's worth of developer time and a year's
worth of headaches. Enjoy!

## Getting Started
Follow the instructions below.

### Generate Secrets Files
By default, your project will not run because it is missing these files:
`secrets.json` and `secrets.py`. These files are ignored in source control.

Generate these files with:
```
python start.py
```

You will first be prompted to rename your project.

### Setup Vagrant
Whether you're creating a full-fledge web application or working with multiple developers,
it is highly recommended to use a vagrant box as your development environment.

Follow the [Vagrant Setup](https://github.com/codenameyau/django-vanilla/tree/master/vagrant#vagrant-centos-7)
to create and provision your Django Vagrant box.
