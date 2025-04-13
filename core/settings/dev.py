from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t+8*b$jp(-^4&mvixpc82wi4k!*7!oo3_q+3nrxk5ab9it+515"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
    'eveza.id',
    'localhost',
    '127.0.0.1',
    'wagtail'  # Nama container Wagtail di jaringan Docker
]

# CSRF Trusted Origins (wajib untuk HTTPS dan proxy)
CSRF_TRUSTED_ORIGINS = [
    'https://eveza.id',
    'http://wagtail:8000'  # Untuk akses internal Docker
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
