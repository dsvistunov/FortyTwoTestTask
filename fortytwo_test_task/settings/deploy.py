from .common import *
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

