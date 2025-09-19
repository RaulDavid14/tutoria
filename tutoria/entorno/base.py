from pathlib import Path
from .credenciales import *
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = PROJECT_KEY


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'core',
    'panel_app',
    'tutoria_app',
    'catalogos_app',
    'usuarios_app',
    'home_app',
    'landing_app',
]

THIRD_PARTY_APPS = [
    'rest_framework',
]


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS  

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # cantidad por defecto
}

# Tiempo en segundos (ejemplo: 30 minutos)
SESSION_COOKIE_AGE = 30 * 60 

# Para que la sesión se renueve en cada request
SESSION_SAVE_EVERY_REQUEST = True  

# Para que la cookie se borre al cerrar el navegador (opcional)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  

STATIC_ROOT = BASE_DIR / "staticfiles"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tutoria.urls'

AUTH_USER_MODEL = 'usuarios_app.UsuarioModel'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tutoria.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'