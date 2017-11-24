"""
Script: start.py

Description:
This script is used to setup a new django-vagrant-box project.
Generates a `secrets.py` settings file and a `secrets.json` secret key.

Important! Run in this Order:
1. `python start.py`
2. `vagrant up`
3. `vagrant ssh`
4. `./manage.py syncdb`
"""
from random import choice
import textwrap
import json
import os.path
import sys


################################################################
# RENAME PROJECT SCRIPT
################################################################
def substitute_text(filepath, old, new):
    data = ''
    with open(filepath, 'r') as fin:
        data = fin.read()
    with open(filepath, 'w') as fout:
        fout.write(data.replace(old, new))

def rename_project():
    old_name = 'vanilla'

    # This script should only be run once.
    if not os.path.exists(old_name):
        sys.exit("Exit: You should only run this script once.")

    # Enter new project name from input.
    new_name = raw_input('Enter your project name: ').lower().replace(' ', '')
    new_name = new_name if new_name else old_name
    filetypes = ('.py', 'bashrc')

    # Substite text in python source files.
    for path, dirs, files in os.walk('.'):

        # Ignore hidden files.
        if path.startswith('./.'):
            continue

        # Match filenames in filetypes, but ignore 'start.py'
        for filename in files:
            if filename != __file__ and filename.endswith(filetypes):
                filepath = '{0}/{1}'.format(path, filename)
                substitute_text(filepath, old_name, new_name)

    # Rename project directory.
    os.rename(old_name, new_name)
    print("\nSuccessfully renamed project to: '{0}'".format(new_name))
    return new_name


################################################################
# GENERATE SECRETS SCRIPT
################################################################
def create_file(file_path, text):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as fp:
            fp.write(text)
            print("File created: '{0}'".format(file_path))
    else:
        print("File already exists: '{0}'".format(file_path))

def generate_secret_key():
    return ''.join([
        choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        for i in xrange(50)])

def create_secrets_json():
    secrets = json.dumps({
        'SECRET_KEY': generate_secret_key(),
    }, indent=4, sort_keys=True)
    create_file('secrets.json', secrets)

def create_secrets_python(project):
    secrets_boilerplate = textwrap.dedent(
    '''
    """
    Django settings for sensitive information.

    Please include any Django settings which may contain sensitive
    information here. This file is ignore by default, and should not
    be added to source control.

    Database Configuration Documentation:
    https://docs.djangoproject.com/en/1.7/ref/settings/#databases
    """

    ################################################################
    # SECERETS DATABASE SETTINGS
    ################################################################
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'vagrant',
            'USER': 'vagrant',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '5432'
        }
    }

    ################################################################
    # SECERETS EMAIL SETTINGS
    ################################################################
    DEFAULT_FROM_EMAIL = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    ''')
    create_file(project+'/settings/secrets.py', secrets_boilerplate)


def main():
    project = rename_project()
    create_secrets_python(project)
    create_secrets_json()

if __name__ == '__main__':
    main()
