"""
Django settings for musicplatform project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from os import path
from pathlib import Path
import os.path  
import sys
from telnetlib import LOGOUT
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^kc%30b0xi!rzdszc+)uxbb-7%d3cjethlyj=t#lu*vorvi#mm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

import mimetypes
mimetypes.add_type("text/css", ".css", True)
# Application definition

INSTALLED_APPS = [
  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'albums',
    'artists',
    'accounts',
    'widget_tweaks',
    'imagekit',
   
    'django_extensions',
  
    'authentication',
    'knox',
    'users',
    'rest_framework',
    
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'musicplatform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
DEFAULT_SQLITE_ENGINES = (
    'django.db.backends.sqlite3',
    'django.db.backends.spatialite',
)
DEFAULT_MYSQL_ENGINES = (
    'django.db.backends.mysql',
    'django.contrib.gis.db.backends.mysql',
    'mysql.connector.django',
)
DEFAULT_POSTGRESQL_ENGINES = (
    'django.db.backends.postgresql',
    'django.db.backends.postgresql_psycopg2',
    'django.db.backends.postgis',
    'django.contrib.gis.db.backends.postgis',
    'psqlextra.backend',
    'django_zero_downtime_migrations.backends.postgres',
    'django_zero_downtime_migrations.backends.postgis',
)

WSGI_APPLICATION = 'musicplatform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
      #  STATIC_ROOT=os.path.join(BASE_DIR, "staticfiles")
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3")),
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
STATIC_DIRS=[
    os.path.join(BASE_DIR,'static'),
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ( 
        'rest_framework.authentication.SessionAuthentication',
    ),
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication', ),
}
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    
    
    
}
REST_FRAMEWORK = {
   
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
    
    'rest_framework.authentication.TokenAuthentication', 
 
)

}
SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout'
}
REST_FRAMEWORK = {
    
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ]
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

AUTH_USER_MODEL='users.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
MEDIA_URL='/media/'
LOGOUT_REDIRECT_URL='home'
TEST_RUNNER = 'my_project.runner.PytestTestRunner'