# django-vanilla
Django-1.7 boilerplate with best practices from *Two Scoops of Django*.
Guaranteed to save you a week's worth of developer time and a year's
worth of headaches. Enjoy!

### Getting Started
Install requirements with: `pip install -r development.txt`

Then create `secrets.json` in the project directory with the following:
```json
{
  "SECRET_KEY": ""
}
```

Run `./manage generate_secret_key` and save that secret key inside your `secrets.json`.

### Choosing Settings File
The default settings file used is `vanilla.settings.base`. You can configure
which settings file to use with command line arguments or with environment variables.

See the [Choosing Django Settings wiki page](https://github.com/codenameyau/django-vanilla/wiki/Choosing-Django-Settings).

### Vagrant
Whether you're creating a full-fledge web application or working with multiple developers,
it is highly recommended to use a vagrant box as your development environment.

See the [Vagrant wiki page](https://github.com/codenameyau/django-vanilla/wiki/Vagrant).

### Design Philosophies
See the [Design Philosophies wiki page](https://github.com/codenameyau/django-vanilla/wiki/Design-Philosophies).
