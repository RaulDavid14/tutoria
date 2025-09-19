from .base import *

DEBUG = True

ALLOWED_HOSTS = ['tutorito.pythonanywhere.com']

database = 'tutorito$tutoria'
user = 'tutorito'
password = 'UdeG.2025'
host = 'tutorito.mysql.pythonanywhere-services.com'
port = '3306'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': database,
        'USER': user,
        'PASSWORD': password,
        'HOST': host,  
        'PORT': port,  
    },
}

