from .base import *


DEBUG = False
SERVE_MEDIA = False

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'app-version',
    'content-type',
    'authorization'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'farmster_prod',
        'USER': 'farmster_admin',
        'PASSWORD': 'TCLaEfQyc9rBK4fS',
        'HOST': 'localhost',
    }
}

AWS_ACCESS_KEY = ''
AWS_ACCESS_SECRET = ''
AWS_REGION = ''

AFRICA_TALKING_USERNAME = 'Farmsterbot'
AFRICA_TALKING_API_KEY = '82039cd015c751c75305eaab667eccf77a13ac1c11ea7e4efda320223cb166bc'
