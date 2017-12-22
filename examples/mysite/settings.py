# Django settings for oauth2app example mysite project.

import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

# Root path of project
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))
# Add SITE_ROOT to python path
SITE_ROOT = os.path.join(PROJECT_ROOT, 'mysite')
sys.path.insert(1, SITE_ROOT)

# Add apps to python path
APP_PATH = os.path.join(SITE_ROOT, 'apps')
sys.path.insert(1, APP_PATH)

# add PROJECT_ROOT to python path
sys.path.insert(1, PROJECT_ROOT)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mysite.sqlite',
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

STATIC_ROOT = '/data/media/oauth2app/example/mysite/static/'

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
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

MY_TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
    os.path.join(SITE_ROOT, 'static'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': MY_TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.base',
    'apps.client',
    'apps.account',
    'apps.oauth2',
    'apps.api',
    'crispy_forms',
    'oauth2app',
    'django_nose',
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

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

CRISPY_TEMPLATE_PACK = 'uni_form'

ALLOWED_HOSTS = ['*', ]
