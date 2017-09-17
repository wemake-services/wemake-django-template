# -*- coding: utf-8 -*-

"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from server.settings.components import BASE_DIR, CONFIG  # NOQA

# Build paths inside the project like this: join(BASE_DIR, ...)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

SECRET_KEY = CONFIG['DJANGO_SECRET_KEY']

# Application definition:

INSTALLED_APPS = (
    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Security:
    'axes',

    # Your apps go here:
    'main_app',
)

MIDDLEWARE = (
    # Django:
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        # Choices are: postgresql_psycopg2, mysql, sqlite3, oracle
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        # Database name or filepath if using 'sqlite3':
        'NAME': CONFIG['POSTGRES_DB'],

        # You don't need these settings if using 'sqlite3':
        'USER': CONFIG['POSTGRES_USER'],
        'PASSWORD': CONFIG['POSTGRES_PASSWORD'],
        'HOST': CONFIG['DJANGO_DATABASE_HOST'],
        'PORT': CONFIG['DJANGO_DATABASE_PORT'],
    },
}


# Security
# https://docs.djangoproject.com/en/1.11/ref/settings/#csrf-cookie-httponly

CSRF_COOKIE_HTTPONLY = True


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    # ('ru', 'Russian'),
    ('en', 'English'),
)

LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Templates
#

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # default template context processors
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },

}, ]

# Media files
# Media-root is commonly changed in production
# (see development.py and production.py).

MEDIA_URL = '/media/'

# Django default authentication system.
# https://docs.djangoproject.com/en/1.11/topics/auth/

# AUTH_USER_MODEL = 'auth_app.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/login-error/'

SESSION_COOKIE_HTTPONLY = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
