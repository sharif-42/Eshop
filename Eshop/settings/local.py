from Eshop.settings.base import *

INSTALLED_APPS += [
    'silk',                     # https://github.com/jazzband/django-silk"
]

# Django silk middleware
MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware'
]

# Django Silk
SILKY_PYTHON_PROFILER = True
