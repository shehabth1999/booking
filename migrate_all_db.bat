@echo off

rem make migrations
python manage.py makemigrations

rem Migrate the default database
python manage.py migrate

rem Migrate the second database
python manage.py migrate --database=second

rem run server
python manage.py runserver