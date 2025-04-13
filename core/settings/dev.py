from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t+8*b$jp(-^4&mvixpc82wi4k!*7!oo3_q+3nrxk5ab9it+515"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CSRF_TRUSTED_ORIGINS = [
    "https://claverio.com",
]

try:
    from .local import *
except ImportError:
    pass
