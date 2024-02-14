import os 
from my_project.settings import *

import django_on_heroku

SECRET_KEY = os.environ.get("SECRET_KEY")

MIDDLEWARE += ("whitenoise.middleware.WhiteNoiseMiddleware",)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEBUG = False
TEMPLATE_DEBUG = False

# ALLOWED_HOSTS = ["*"]


django_on_heroku.settings(locals())

