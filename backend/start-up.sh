#!/bin/bash

python3 manage.py migrate --no-input
pythn3 manage.py collectstatic

while true; do
    # python3 manage.py runserver 0.0.0.0:8000
    gunicorn backend.wsgi -b 0.0.0.0:8000
    sleep 5s
done