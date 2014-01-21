import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': 'reservations.sqlite'}}

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'INFO',
            'handers': ['console'],
        },
    },
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

