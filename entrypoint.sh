#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo 'Performing migrations...'
python manage.py migrate

echo 'Creating superuser...'
python manage.py createsuperuser_credentials

exec "$@"
