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
        'PASSWORD': 'fShW52pY6YZTeerT',
        'HOST': '/cloudsql/farmster-ee483:us-central1:farmster-prod-db'
    }
}

AWS_ACCESS_KEY = ''
AWS_ACCESS_SECRET = ''
AWS_REGION = ''

AFRICA_TALKING_USERNAME = 'Farmsterbot'
AFRICA_TALKING_API_KEY = '82039cd015c751c75305eaab667eccf77a13ac1c11ea7e4efda320223cb166bc'

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'farmster_media'
GS_ACCESS_KEY_ID = 'GOOG1EYXYISKGWFWE6ZOMTFMB5R3EHR7WDU572KJLWP3QYRJVX536IQXIKE5I'
GS_SECRET_ACCESS_KEY = 'lPMdwVkK5qgz/odvaOJZslo4wq1jhYtSk5ROP2bv'
