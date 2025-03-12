web: gunicorn ecommerce.wsgi --log-file -
#or works good on external database
web: python manage.py migrate && gunicorn ecommerce.wsgi