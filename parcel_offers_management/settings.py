"""
======================================================================
Project Name: Parcel Offers Management System
Description:
    A backend API project for managing offers on predefined parcels
    of land. This project includes features for handling brokers,
    parcels, and offers, along with background jobs for monitoring
    and notification.

Author: Mohamed Riyad
Email: mohamed@ryad.dev
Website: https://ryad.dev

License: MIT License
======================================================================
"""

from pathlib import Path
import environ

# Initialize environment variables
env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

# Read .env file if it exists
environ.Env.read_env(env_file=str(BASE_DIR / '.env'))

# Read the value of the ENV environment variable
ENV = env('ENV', default='development')

# Ensure SECRET_KEY is provided in production
if ENV == 'production':
    # In production, the SECRET_KEY is stored in the
    # environment variables and not in the settings file
    SECRET_KEY = env('SECRET_KEY')
else:
    # Using a dummy default value for SECRET_KEY in development
    SECRET_KEY = env('SECRET_KEY', default='development-secret-key')

NOTIFICATION_SERVICE_API_URL = env('NOTIFICATION_SERVICE_API_URL', default='https://dummyjson.com/http/200/notify')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'apps.parcels',
    'apps.brokers',
    'apps.offers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.token_auth.TokenAuthenticationMiddleware',  # For token-based authentication
]

ROOT_URLCONF = 'parcel_offers_management.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'parcel_offers_management.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME', default='default_db'),
        'USER': env('DB_USER', default=None),  # No default value, optional
        'PASSWORD': env('DB_PASSWORD', default=None),  # No default value, optional
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.custom_exception_handler.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Number of records per page
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
