from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('RDS_DATABASE'),
        'USER': env('RDS_USER'),
        'PASSWORD': env('RDS_PASSWORD'),
        'HOST': env('RDS_HOST'),
        'PORT': env('RDS_PORT'),
    }
}
