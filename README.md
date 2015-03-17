# django-vanilla
Django boilerplate with Two Scopes best practices.

## Running Application

#### Manually specify settings
You can either manually specify which settings file to use:

Base:
`./manage.py runserver`

Local / Development:
`./manage.py runserver --settings=vanilla.settings.local`

Staging:
`./manage.py runserver --settings=vanilla.settings.staging`

Production:
`./manage.py runserver --settings=vanilla.settings.production`

#### Set Environment variable
Or set your `DJANGO_SETTINGS_MODULE` environment variable,
either manually or add it to your `.bashrc` or `.bash_profile`.

Like so:
`export DJANGO_SETTINGS_MODULE="vanilla.settings.local"`

If you're using a python virtual environment add the statement
above in the end of your `/bin/active`.
