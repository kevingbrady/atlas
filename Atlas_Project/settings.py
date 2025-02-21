"""
Django settings for Atlas_Project project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import mongoengine

import sys

mongoengine.connect('Atlas', host='localhost', port=27017)


COLLECTION_NAMES = {

    'cybersecurity_threats': 'Atlas_cybersecurity_threats',
    'actors': 'Atlas_actors',
    'responding_organizations': 'Atlas_responding_organizations',
    'technologies': 'Atlas_technologies',
    'disciplines': 'Atlas_disciplines',
    'locations': 'Atlas_locations',
    'information_types': 'Atlas_information_types',
    'information_categories': 'Atlas_information_categories',
    'activities': 'Atlas_activities',
    'use_cases': 'Atlas_UseCases'
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (True, False)[len(sys.argv) > 2]
#TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['localhost', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_mongoengine',
    'webpack_loader',
    'Atlas',
    'Atlas_Project'
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

ROOT_URLCONF = 'Atlas_Project.urls'
INTERNAL_IPS = ('127.0.0.1',)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
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

WSGI_APPLICATION = 'Atlas_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Atlas'
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

BUNDLE_DIR = os.path.join(STATIC_ROOT, "bundles")
DEVELOPMENT_BUNDLE_DIR = os.path.join(STATIC_ROOT, "bundles", "development")
PRODUCTION_BUNDLE_DIR = os.path.join(STATIC_ROOT, "bundles", "production")

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': os.path.join('bundles', 'development'),  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

if not os.path.exists(STATIC_ROOT):
    os.mkdir(STATIC_ROOT)

if not os.path.exists(BUNDLE_DIR):
    os.mkdir(BUNDLE_DIR)

if not os.path.exists(DEVELOPMENT_BUNDLE_DIR):
    os.mkdir(DEVELOPMENT_BUNDLE_DIR)

if not os.path.exists(PRODUCTION_BUNDLE_DIR):
    os.mkdir(PRODUCTION_BUNDLE_DIR)

if not DEBUG:
    WEBPACK_LOADER['DEFAULT'].update({
        'BUNDLE_DIR_NAME': os.path.join('bundles', 'production'),
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json')
    })


STATICFILES_DIRS = [
    DEVELOPMENT_BUNDLE_DIR,
    PRODUCTION_BUNDLE_DIR
]