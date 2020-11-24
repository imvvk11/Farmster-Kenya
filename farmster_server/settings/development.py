from .base import *

DEBUG = True
SERVE_MEDIA = True

ALLOWED_HOSTS = ['*']
ALLOWED_METHODS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'app-version',
    'content-type',
    'authorization'
)
# Database has been changed for UAT Testing. You can configure your database with credentials here...
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'farmster_dev',
        'USER': 'farmster_admin',
        'PASSWORD': 'TCLaEfQyc9rBK4fS',
        'HOST': 'localhost'
    }
}



AWS_ACCESS_KEY = ''
AWS_ACCESS_SECRET = ''
AWS_REGION = ''

AFRICA_TALKING_USERNAME = 'Farmsterbot'
AFRICA_TALKING_API_KEY = '82039cd015c751c75305eaab667eccf77a13ac1c11ea7e4efda320223cb166bc'
