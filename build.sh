#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input

  print('Superuser has been created.')
fi