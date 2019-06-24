release: python manage.py migrate
release: python manage.py migrate auth
release: python manage.py migrate --run-syncdb
release: python manage.py loaddata db.json
web: gunicorn project.wsgi