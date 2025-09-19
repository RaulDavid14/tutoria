import os
import sys

path = '/home/tutorito/tutoria'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'tutoria.entorno.produccion'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
