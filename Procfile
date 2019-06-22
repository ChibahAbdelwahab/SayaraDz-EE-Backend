release: python manage.py migrate auth
release: python manage.py migrate --run-syncdb
release: restart
release: pg:reset DATABASE
web: gunicorn project.wsgi