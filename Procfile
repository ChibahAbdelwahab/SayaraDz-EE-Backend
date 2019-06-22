release: python manage.py migrate auth
release: python manage.py migrate --run-syncdb
web: gunicorn project.wsgi