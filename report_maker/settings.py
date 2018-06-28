"""
Django settings for report_maker project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(BASE_DIR + '/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()  # read text and skip sign of new line "\n"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'main_page'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'report',
    'account',
    'connection',
    'report_maker',
    'social_django',
    'facebook',

    'django_extensions',  # using for development process
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'report_maker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',  # <--
            ],
            'libraries':{
                'filters': 'connection.templatetags.filters',
                'datetime_filters': 'report.templatetags.datetime_filters',

            },
        },
    },
]


WSGI_APPLICATION = 'report_maker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'report_maker_db.sqlite3'),
    },

    'production': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'report_maker_db',
        'USER': 'report_maker_user',
        'PASSWORD': 'jeferson97',
        'HOST': 'localhost',  # Set to empty string for localhost.
        'PORT': '5432',  # Set to empty string for default.
    },
}


AUTHENTICATION_BACKENDS = [
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'account.backends.UserAuth',
]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

with open(BASE_DIR + '/facebook_app_settings.txt') as f:
    SOCIAL_AUTH_FACEBOOK_KEY = f.readline().strip()  # App ID
    SOCIAL_AUTH_FACEBOOK_SECRET = f.readline().strip()  # App Secret

with open(BASE_DIR + '/twitter_app_settings.txt') as f:
    SOCIAL_AUTH_TWITTER_KEY = f.readline().strip()  # read line and skip sign of new line "\n"
    SOCIAL_AUTH_TWITTER_SECRET = f.readline().strip()  # read line and skip sign of new line "\n"


SOCIAL_AUTH_FACEBOOK_SCOPE = ['user_posts']

SOCIAL_AUTH_LOGIN_ERROR_URL = 'main_page'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'main_page'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
# Force https redirect
SECURE_SSL_REDIRECT = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Force HTTPS in the final URIs
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
# Use this server address as default using
# './manage.py runserver_plus --cert /tmp/cert' command in terminal during development process
RUNSERVERPLUS_SERVER_ADDRESS_PORT = '127.0.0.1:9000'
