"""
Django settings for devpay project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b&td)r^a1hd#2#^3s@mft)5@-k&31s7n=k2w!yt$b-7uo2#phj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'donations',
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

ROOT_URLCONF = 'devpay.urls'

WSGI_APPLICATION = 'devpay.wsgi.application'
BT_MERCH_ID = '9ttpz4pht63y3rtb'
BT_PUBKEY = '726d9275ynn58gj4'
BT_CSEKEY = r'MIIBCgKCAQEAyoMWwTpd2kqDBsXrQG0sDA4kjthSI+732cRARAmWXSk2XPRpVxV+XunVL3TMd96FE2u3k55IK1yEQ7hPCGNsRIiYpFR4Y2fgXYpKkZ6s6O1JYi1X0QKSrdU8lR3Xg5AdxBKZMzdh8RJmSFpOUtk/Gbn3Ls4TfMgAoINpyG1OOfZdfJ9N1JQ6RSkvOoP21sAdwsc+TBc0bCYIprF61k7hoD+hedbv0H8F6uCH44MANC6eCHkzDCZbKi0t7PIgpt+AufilAnYTMIhDNDeANf2T8pYR04T1RAn39M0w+34W6bd/+FZXi5zM45CUeEZ7MJ2xTXGAg7P63QQkHxAFBr1SpQIDAQAB'
BT_PRIVATE_KEY = r'9e851b8fce7317452e4c7b768422670b' 

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
