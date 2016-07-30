import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "semestrovka_django_2k.settings")

application = get_wsgi_application()
