import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OIL_PAINTING_BE.settings')

application = get_wsgi_application()
