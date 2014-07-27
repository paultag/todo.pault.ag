import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = os.environ.get("SECRET_KEY", '')
DEBUG = os.environ.get("DJANGO_DEBUG", False)
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'public.urls'
WSGI_APPLICATION = 'public.wsgi.application'


TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
)

DATABASES = {
    'default': dj_database_url.parse(os.environ.get(
        'DATABASE_URL',
        'postgres://todo:todo@localhost/todo'
    ))
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
