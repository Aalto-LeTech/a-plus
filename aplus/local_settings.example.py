#DEBUG = True
#SECRET_KEY = '' # will be autogenerated in secret_key.py if not specified here
#BASE_URL = 'http://localhost:8000/' # required!
#SERVER_EMAIL = 'your_email@domain.com'
#ADMINS = (
#    ('Your Name', 'your_email@domain.com'),
#)
## Branding
#BRAND_NAME = 'Your brand name (default is A+)'
#BRAND_DESCRIPTION = 'Description of your service (default is Virtual Learning Environment)'
# BRAND_INSTITUTION_NAME = Your institution name, e.g., 'Aalto University', 'Tampere university'
# Show red alert on top of all pages
#SITEWIDE_ALERT_TEXT = "Maintenance on Monday"
#SITEWIDE_ALERT_TEXT = {'en': "Maintenance on Monday", 'fi': "Maanantaina on palvelukatko"}
# Show blue info box on course index and course menu
#SITEWIDE_ADVERT = {
#    'not-before': '2020-01-01', # start showing on 1st
#    'not-after': '2020-01-04', # last visible date is 3rd
#    'title': {'en': "Advert", 'fi': "Mainos"},
#    'text': {'en': "We have open positions",
#             'fi': "Meillä on paikkoja"}
#    'href': "https://apluslms.github.io",
#    'image': "https://apluslms.github.io/logo.png",
#}


## Authentication backends
#INSTALLED_APPS += (
#    'shibboleth_login',
#    'social_django',
#)

## Shibboleth options
#SHIBBOLETH_ENVIRONMENT_VARS = {
#    # required for the shibboleth system:
#    'PREFIX': 'SHIB_', # apache2: SHIB_, nginx: HTTP_SHIB_ (NOTE: client can inject HTTP_ vars!)
#    'STUDENT_DOMAIN': 'example.com', # domain where student numbers are selected
#    # ..more options in aplus/settings.py
#}

## Database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'your_db_name',
#        # use ident auth for local servers
#        # and add passwd&hostname etc for remote
#    }
#}

## Caches
#CACHES = {
#    'default': {
#        # prefer memcached with unix socket
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': 'unix:/tmp/memcached.sock',
#
#        # Database cache, if memcached is not possible
#        # remember to run `./manage.py createcachetable`
#        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#        'LOCATION': 'django_cache_default',
#
#        # Local testing with max size
#        'BACKEND': 'lib.cache.backends.LocMemCache',
#        'LOCATION': 'unique-snowflake',
#        'OPTIONS': {'MAX_SIZE': 1000000}, # simulate memcached value limit
#
#        # or dummy
#        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#    }
#}

## Logging
# For debugging purposes
#from .settings import LOGGING
#LOGGING['loggers'].update({
#    '': {
#        'level': 'INFO',
#        'handlers': ['debug_console'],
#        'propagate': True,
#    },
#    'django.db.backends': {
#        'level': 'DEBUG',
#    },
#})
