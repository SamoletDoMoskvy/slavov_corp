#! /bin/bash

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --force

exec gunicorn -c gunicorn.py slavov_backend.asgi:application -k uvicorn.workers.UvicornWorker --reload
