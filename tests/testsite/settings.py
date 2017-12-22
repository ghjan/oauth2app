# Django settings for oauth2app example mysite project.

import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Root path of project
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))

# Add projects to python path
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'mysite')
sys.path.insert(1, PROJECT_PATH)
# Add apps to python path
APP_PATH = os.path.join(PROJECT_ROOT, 'apps')
sys.path.insert(1, APP_PATH)

sys.path.insert(1, PROJECT_ROOT)
print("sys.path:{}".format(sys.path))

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testsite.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

FIXTURE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'apps/account/fixtures'),
)

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

LOGIN_URL = "/account/login"

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '=hf03e+08xlolbb$!-s01m-n_4xn*5mdsd!pm@$+ms!pe08f-7'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'testsite.urls'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testsite.apps.api',
    'testsite.apps.oauth2',
    'oauth2app')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# TEST_RUNNER = 'django-test-coverage.runner.run_tests'
# COVERAGE_MODULES = (
#     'oauth2app.authenticate',
#     'oauth2app.authorize',
#     'oauth2app.models',
#     'oauth2app.token',
#     'oauth2app.lib.uri',)
