from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#ij84d6w2h(l#7*3buc*zu9@stq-p1#lv)jwlyj0=^!txbm%@='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#para seql server
"""
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'TPFINAL',
        'Trusted_Connection':'yes',
        'HOST': 'localhost',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}
"""
