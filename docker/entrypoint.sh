#!/bin/sh
set -x

echo "Database is ready"

python manage.py makemigrations
python manage.py migrate
python collectstatic --noinput
exec "$@"
