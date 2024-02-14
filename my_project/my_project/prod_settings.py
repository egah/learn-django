import os 
from my_project.settings import *

import django_on_heroku

'''
MIDDLEWARE += ("whitenoise.middleware.WhiteNoiseMiddleware",)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["*"]
'''

SECRET_KEY = os.environ.get("SECRET_KEY")

django_on_heroku.settings(locals())

