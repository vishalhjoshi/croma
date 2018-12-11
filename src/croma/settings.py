#  pg_dump -d croma --host=localhost --port=5432 --username=postgres --password=root --clean    > backup 
#  psql -d croma -U postgres -f backup     

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'l(_o&qjy@nk1q8o*nq2u3wf#*z85k=&7hkyn$@rllsllv-z*7&'

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'accounts',
    'item_master',
    'unit_master',
    'company_master',
    'salt_master',
    'godown_master',
    'home',
    'sales',
    'purchase'
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DBBACKUP_STORAGE_OPTIONS = {'location': "E:/backup/"}




REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],


}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    'rest_backend': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }

}


SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
CACHE_MIDDLEWARE_KEY_PREFIX = 'croma'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',


    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'croma.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'croma.wsgi.application'

# try:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'croma',
#         'USER': 'postgres', #'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# except:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'croma',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'PORT': '5432',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on

#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


log_file = os.path.join(os.path.dirname(BASE_DIR), "logs/views.log")
logging.basicConfig(format='%(asctime)s  %(levelname)-8s [%(name)s: %(lineno)d]  %(message)s',
                    datefmt='%d-%m-%Y:%H:%M',
                    level=logging.ERROR, filename=log_file)


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
USE_L10N = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")
