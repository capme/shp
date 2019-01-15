from os import environ
from .base import *

THIRD_PARTY_APPS = (
    'django_nose',  # for unittest using this package
)

INSTALLED_APPS += THIRD_PARTY_APPS

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': environ.get('POSTGRES_USER', 'postgresuser'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 'mysecretpass'),
        'HOST': environ.get('POSTGRES_HOST', 'postgres'),
        'PORT': environ.get('DB_PORT', '5432'),
        'ATOMIC_REQUESTS': True,
    }
}

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

PYREBASE_MOCK = True
BROKER_BACKEND = 'memory'
