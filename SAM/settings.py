"""
Django settings for SAM project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-h5$(z4_03@@-a!x(#4(!@a!&vu#ium3*=05xcinu+4flz6ob4l"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG=False

ALLOWED_HOSTS = ['student-acc-management.herokuapp.com','127.0.0.1']


# Application definition
DEFAULT_APPS= [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
     'allauth.socialaccount.providers.yahoo',
     
]


MY_APPS=['home.apps.HomeConfig',]
THIRD_PARTY_APPS=[ 'widget_tweaks',
                   'crispy_forms',
                   'rest_framework',
                   'django_filters',
                   
                   
                  ]

INSTALLED_APPS =DEFAULT_APPS+ MY_APPS+THIRD_PARTY_APPS
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "SAM.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [
   'django.contrib.auth.backends.ModelBackend',
   'allauth.account.auth_backends.AuthenticationBackend',
   
]

WSGI_APPLICATION = "SAM.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

import os

STATIC_URL = "static/"

STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static')
]
GOOGLE_API_KEY='AIzaSyC4Sbdhtf_jXVXwo96YFyECThF0_Ji91aA'

RECAPTCHA_KEY='6Ldjn3siAAAAANctNxOZ8zKxIpkmhG4cORBOEBoF'
RECAPTCHA_SECERT_KEY='6Ldjn3siAAAAAFLK7-4a2u1BRGH62sCwwGzoQpLp'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


SITE_ID = 2
LOGIN_REDIRECT_URL = "house"
ACCOUNT_SIGNUP_REDIRECT_URL = "login"
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
       'SCOPE':[
           'profile',
           'email',
       ],
        'AUTH_PARAMS': {
            'access_type':'online',
        }
    },
    'yahoo': {
       'SCOPE':[
           'profile',
           'email',
       ],
        'AUTH_PARAMS': {
            'access_type':'online',
        }
    }
}

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# ACCOUNT_AUTHENTICATION_METHOD="email"
# ACCOUNT_EMAIL_REQUIRED=True
# ACCOUNT_EMAIL_VERIFICATION="mandatory"
# ACCOUNT_USERNAME_REQUIRED =False

#simple mail transfer protocol
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='samdjango8000@gmail.com'
EMAIL_HOST_PASSWORD='django$123'


CRISPY_TEMPLATE_PACK="bootstrap4"