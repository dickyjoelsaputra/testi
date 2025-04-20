from .base import *


# print("!!! USING DEV SETTINGS !!!")
# print(f"DB_HOST from env: {os.getenv('DB_HOST')}")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key-if-env-not-set")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
    'eveza.id',
    'localhost',
    '127.0.0.1',
    'wagtail'  # Nama container Wagtail di jaringan Docker
]

# CSRF Trusted Origins (wajib untuk HTTPS dan proxy)
CSRF_TRUSTED_ORIGINS = os.getenv(
    "CSRF_TRUSTED_ORIGINS",
    "https://eveza.id,http://wagtail:8000"
).split(",")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Override static settings for local development
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'

# STORAGES = {
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
#     },
# }

try:
    from .local import *
except ImportError:
    pass
