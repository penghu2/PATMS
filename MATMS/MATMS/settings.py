"""
Django settings for MATMS project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5b!hzyu4)fb!vascx+-(aph2w)*=jd%k#tp7o!#5imaw*3l%-_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'XTest',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MATMS.urls'

WSGI_APPLICATION = 'MATMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'KuyinPTest',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '172.16.95.34',
        'PORT': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT =''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'

PROJECT_DIR = ''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(name)s %(asctime)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(name)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'django_request':{
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s status_code:%(status_code)d',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'django_db_backends':{
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s duration:%(duration).3f sql:%(sql)s params:%(params)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'custom_log_file':{
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, 'logs/django.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'verbose'
        },
        'django_request_logfile':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, 'logs/django_request_logfile.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'django_request'
        },
        'django_db_backends_logfile':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, 'logs/django_db_backends_logfile.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'django_db_backends'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins','django_request_logfile'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['django_db_backends_logfile',],
            'level': 'WARNING',
            'propagate': True,
        },
        'customapp': {#then you can change the level to control your custom app whether to output the debug infomation
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'customapp.engine': {#then you can change the level to control your custom app whether to output the debug infomation
            'handlers': ['custom_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

