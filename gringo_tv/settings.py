"""
Django settings for Gringo TV project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import cloudinary
from decouple import Csv
from decouple import config
from django.urls import reverse_lazy
from dj_database_url import parse as dburl
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPEND_SLASH = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=['*'], cast=Csv())

SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)

# Application definition

INSTALLED_APPS = [
    'gringo_tv.core.apps.CoreConfig',
    'gringo_tv.core.apps.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTRA_APPS = [
    'gringo_tv.core.apps.AuditlogCustomConfig',
    'test_without_migrations',
    'widget_tweaks',
    'django_extensions',
    'storages',
    'cloudinary'
]

PROJECT_APPS = [
    'gringo_tv.custom_profile.apps.CustomProfileConfig',
    'gringo_tv.dealer.apps.DealerConfig',
]

INSTALLED_APPS += EXTRA_APPS
INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

ROOT_URLCONF = 'gringo_tv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'gringo_tv.core.context_processors.debug',
            ],
        },
    },
]

WSGI_APPLICATION = 'gringo_tv.wsgi.application'

LOGIN_URL = reverse_lazy('profile:login')
LOGIN_REDIRECT_URL = reverse_lazy('core:home')
LOGOUT_REDIRECT_URL = reverse_lazy('profile:login')


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('pt_BR', _('Brazilian Portuguese')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# AWS_QUERYSTRING_AUTH = True
# AWS_DEFAULT_ACL = 'private'
# AWS_BUCKET_ACL = 'private'
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_AWS_BUCKET = config('STATIC_AWS_BUCKET', default='')
STATICFILES_STORAGE = config('STATICFILES_STORAGE', default='django.contrib.staticfiles.storage.StaticFilesStorage')

MEDIA_URL = config('MEDIA_URL', default='/media/')
# MEDIA_AWS_BUCKET = config('MEDIA_AWS_BUCKET', default='')

DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', default='django.core.files.storage.FileSystemStorage')

if DEFAULT_FILE_STORAGE == 'django.core.files.storage.FileSystemStorage':
    MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'gringo_tv/media'))

# Email configuration

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = config('SERVER_EMAIL')

# CLOUDINARY
CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME', default='')
CLOUDINARY_API_KEY = config('CLOUDINARY_API_KEY', default='')
CLOUDINARY_API_SECRET = config('CLOUDINARY_API_SECRET', default='')

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)
