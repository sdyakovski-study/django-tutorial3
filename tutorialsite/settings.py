"""
Django settings for tutorialsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# settings.py will be read and evaluated on the project level (possibly by manage.py).
# BASE_DIR points to the '/home/sdyakovski/projects/python-projects/django-tutorial3/project'
# but is dealing with relative paths, not absolute paths, so its value from manage.py would be ''.
# It simply starts with __file__ (which is settings.py); its dirname (tutorialsite); and its dirname (project),
# which is the curdir of manage.py => '' 

# ADD EXTERNALS PATHS TO sys.path
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# BASE_PATH is abspath of 'tutorialsite/..', which is 
# '/home/sdyakovski/projects/python-projects/django-tutorial3/project'
# - which is the same dir as BASE_DIR, but absolute (needed for sys.path)
EXTERNAL_LIBS_PATH = os.path.join(BASE_PATH, 'externals', 'libs')
EXTERNAL_APPS_PATH = os.path.join(BASE_PATH, 'externals', 'apps')
sys.path = ['', EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path[1:]
# [1:] in order to eliminate the first element of the list (''), which is moved to the front
print sys.path

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_PATH is abspath of 'tutorialsite', where __file__ (settings.py) is, which is 
# '/home/sdyakovski/projects/python-projects/django-tutorial3/project/tutorialsite'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r311@qboon)66q@6y2rf(ru$u-30a!_dc%2*l6#+73zxybl&)z'

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
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tutorialsite.urls'

WSGI_APPLICATION = 'tutorialsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
