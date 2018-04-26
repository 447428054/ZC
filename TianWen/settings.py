# -*- coding: utf-8 -*-

import os
from django.conf.global_settings import STATICFILES_FINDERS
import os.path

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRJ_ROOT=os.path.join(BASE_DIR,'..')
#
# DEBUG = False
# ALLOWED_HOSTS= ['*']
#
#
# ADMINS = (
#     # ('Your Name', 'your_email@domain.com'),
# )
#
# MANAGERS = ADMINS
# DEFAULT_CHARSET = 'utf-8'
#
# FILE_CHARSET = 'utf-8'
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'mysql',                      # Or path to database file if using sqlite3.
#         'USER': 'root',                      # Not used with sqlite3.
#         'PASSWORD': 'lizheng',                  # Not used with sqlite3.
#         'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }
#
# # Local time zone for this installation. Choices can be found here:
# # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# # although not all choices may be available on all operating systems.
# # If running in a Windows environment this must be set to the same as your
# # system time zone.
# TIME_ZONE = 'Asia/Shanghai'
# USE_TZ = True
#
# # Language code for this installation. All choices can be found here:
# # http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'zh-hans'
#
# LANGUAGES = (
#     ('ca', 'Catalan'),
#     ('cs', 'Czech'),
#     ('de', 'German'),
#     ('en', 'English'),
#     ('es', 'Spanish'),
#     ('fo', 'Faroese'),
#     ('fr', 'France'),
#     ('it', 'Italian'),
#     ('lt', 'Lithuanian'),
#     ('mn', 'Mongolian'),
#     ('nl', 'Dutch'),
#     ('pl', 'Polish'),
#     ('ru', 'Russian'),
#     ('uk_UA', 'Ukrainian'),
#     ('vi', 'Vietnamese'),
#     ('zh_CN', 'Chinese'),
# )
#
# SITE_ID = 1
#
# # If you set this to False, Django will make some optimizations so as not
# # to load the internationalization machinery.
# USE_I18N = True
# # If you set this to False, Django will not format dates, numbers and
# # calendars according to the current locale
# USE_L10N = True
#
# # Absolute filesystem path to the directory that will hold user-uploaded files.
# # Example: "/home/media/media.lawrence.com/media/"
# MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
#
# # URL that handles the media served from MEDIA_ROOT. Make sure to use a
# # trailing slash.
# # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA_URL = '/media/'
#
# # Absolute path to the directory static files should be collected to.
# # Don't put anything in this directory yourself; store your static files
# # in apps' "static/" subdirectories and in STATICFILES_DIRS.
# # Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
#
# # URL prefix for static files.
# # Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'
#
# # Additional locations of static files
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT,'project_static'),
# )
#
# # List of finder classes that know how to find static files in
# # various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )
#
# # Make this unique, and don't share it with anybody.
#
# if not hasattr(globals(), 'SECRET_KEY'):
#     SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
#     try:
#         SECRET_KEY = open(SECRET_FILE).read().strip()
#     except IOError:
#         try:
#             from random import choice
#             import string
#             symbols = ''.join((string.ascii_lowercase, string.digits, string.punctuation))
#             SECRET_KEY = ''.join([choice(symbols) for i in range(50)])
#             secret = open(SECRET_FILE, 'w')
#             secret.write(SECRET_KEY)
#             secret.close()
#         except IOError:
#             raise Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)
#
#
#
# MIDDLEWARE_CLASSES = (
#     'django.middleware.cache.UpdateCacheMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     # 'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.cache.FetchFromCacheMiddleware',
#
#     'djangobb_forum.middleware.LastLoginMiddleware',
#     'djangobb_forum.middleware.UsersOnline',
#     'djangobb_forum.middleware.TimezoneMiddleware',
# )
#
# ROOT_URLCONF = 'TianWen.urls'
#
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
#         'OPTIONS': {
#             'context_processors': ['django.contrib.auth.context_processors.auth',
#                                    'django.template.context_processors.debug',
#                                    'django.template.context_processors.i18n',
#                                    'django.template.context_processors.media',
#                                    'django.template.context_processors.static',
#                                    'django.template.context_processors.request',
#                                    'django.contrib.messages.context_processors.messages',
#
#                                    'django_messages.context_processors.inbox',
#
#                                    'djangobb_forum.context_processors.forum_settings',
#                                    ],
#             'loaders': [
#                 'django.template.loaders.filesystem.Loader',
#                 'django.template.loaders.app_directories.Loader',
#                 'django.template.loaders.eggs.Loader',
#             ]
#         },
#     },
# ]
#
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',

    'el_pagination',
    'easy_thumbnails',
    'constance',
    'constance.backends.database',
    'djangobower',

    'captcha',
    'rest_framework',

    'lbforum',
    'lbattachment',
    'lbutils',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',

    'haystack',
    'django_messages',
    'nocaptcha_recaptcha',

    'Note',
    'Upload',
    'QA',

)
#
# # A sample logging configuration. The only tangible logging
# # performed by this configuration is to send an email to
# # the site admins on every HTTP 500 error when DEBUG=False.
# # See http://docs.djangoproject.com/en/dev/topics/logging for
# # more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }
#
# try:
#     import mailer
#     INSTALLED_APPS += ('mailer',)
#     EMAIL_BACKEND = "mailer.backend.DbBackend"
# except ImportError:
#     pass
#
#
# FORCE_SCRIPT_NAME = ''
#
# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE':
                   'QA.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'djangobb_index'),
        'INCLUDE_SPELLING': True,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 8
#
# # Account settings
# ACCOUNT_ACTIVATION_DAYS = 10
# LOGIN_REDIRECT_URL = '/forum/'
# LOGIN_URL = '/forum/account/signin/'
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
#
# # Cache settings
# CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#
# # Allauth
# ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_SIGNUP_FORM_CLASS = 'forms.SignupForm'
#
# try:
#     from local_settings import *
# except ImportError:
#     pass



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

SECRET_KEY = 'h(v1^4#eigd5_76vag0$-6=-*&q_^-g!b)9*!$#u$e%v$tudt$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django.contrib.sites',
#
#     'el_pagination',
#     'easy_thumbnails',
#     'constance',
#     'constance.backends.database',
#     'djangobower',
#     'allauth',
#     'allauth.account',
#     'captcha',
#     'rest_framework',
#
#     'lbforum',
#     'lbattachment',
#     'lbutils',
#
#     'Note',
#     'Upload',
#     'QA',
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TianWen.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TianWen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mysql',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'lizheng',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh_Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PRJ_ROOT, 'collectedstatic')

HOST_URL = ''
MEDIA_URL_ = '/media/'
MEDIA_URL = HOST_URL + MEDIA_URL_
MEDIA_ROOT = os.path.join(PRJ_ROOT, 'media')

SIGNUP_URL = '/accounts/signup/'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'
CHANGE_PASSWORD_URL = '/accounts/password/change/'

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'forbidden_words': ('', 'Forbidden words', str),
}

STATICFILES_FINDERS += (('djangobower.finders.BowerFinder'),)

BOWER_COMPONENTS_ROOT = PRJ_ROOT

BOWER_INSTALLED_APPS = (
    'jquery#1.12',
    'markitup#1.1.14',
    'mediaelement#2.22.0',
    'blueimp-file-upload#9.12.5',
)

BBCODE_AUTO_URLS = True
#add allow tags
HTML_SAFE_TAGS = ['embed']
HTML_SAFE_ATTRS = ['allowscriptaccess', 'allowfullscreen', 'wmode']
#add forbid tags
HTML_UNSAFE_TAGS = []
HTML_UNSAFE_ATTRS = []
