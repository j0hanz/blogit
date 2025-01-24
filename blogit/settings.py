"""Django settings for Blogit API."""

import os
from pathlib import Path

import cloudinary
import dj_database_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Flag to detect if in development mode
IS_DEV = 'DEV' in os.environ

# Secret Key
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = IS_DEV

# Allowed Hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if not IS_DEV:
    prod_host = os.getenv('ALLOWED_HOST')
    if prod_host:
        ALLOWED_HOSTS.append(prod_host)

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    'django_filters',
    'debug_toolbar',
    'django_extensions',
    'drf_yasg',
    'rest_framework_simplejwt',
    'profiles',
    'posts',
    'followers',
    'likes',
]

SITE_ID = 1

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'blogit.urls'

# Templates
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

WSGI_APPLICATION = 'blogit.wsgi.application'

# Database Configuration
if IS_DEV:
    print('Using SQLite database (Dev)')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    print('Using Production database')
    DATABASES = {
        'default': dj_database_url.parse(os.getenv('DATABASE_URL', ''))
    }

# Authentication & REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DATETIME_FORMAT': '%a %d-%m-%Y %H:%M',
}

REST_AUTH = {
    'USE_JWT': False,
    'USER_DETAILS_SERIALIZER': 'blogit.serializers.CurrentUserSerializer',
}

# CORS and CSRF
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = IS_DEV

CORS_ALLOWED_ORIGINS = ['https://*.herokuapp.com']
if not IS_DEV:
    client_origin = os.getenv('CLIENT_ORIGIN')
    if client_origin:
        CORS_ALLOWED_ORIGINS.append(client_origin)

CSRF_TRUSTED_ORIGINS = [
    'https://*.herokuapp.com',
]

# Cloudinary Configuration
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
)

STATIC_URL = '/static/'

# Internationalization and Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Stockholm'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
