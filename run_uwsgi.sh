#!/bin/bash
python manage.py syncdb
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi uwsgi.ini