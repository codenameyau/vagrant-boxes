"""
Script: start.py

Description:
This script is used to provision a new django-vagrant-box project.
Generates a `secrets.py` settings file and a `secrets.json` secret key.
"""
from random import choice
import textwrap
import json
import os.path


def save_unwritten_file(file_path, text):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as fp:
            fp.write(text)
            print "File created: '{0}'".format(file_path)
    else:
        print "File already exists: '{0}'".format(file_path)


def generate_secret_key():
    return ''.join([
        choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        for i in range(50)])


def create_secrets_json():
    secrets = json.dumps({
        'SECRET_KEY': generate_secret_key(),
    }, indent=4, sort_keys=True)
    save_unwritten_file('secrets.json', secrets)


def create_secrets_python():
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
    save_unwritten_file('vanilla/settings/secrets.py', secrets_boilerplate)


def main():
    create_secrets_json()
    create_secrets_python()


if __name__ == '__main__':
    main()
