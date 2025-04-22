from .base import *
import os

# MinIO Storage Configuration
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('MINIO_ACCESS_KEY', 'minioadmin')
AWS_SECRET_ACCESS_KEY = os.getenv('MINIO_SECRET_KEY', 'minioadmin')
AWS_STORAGE_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME', 'static')
AWS_S3_ENDPOINT_URL = os.getenv('MINIO_ENDPOINT', 'http://minio:9000')
AWS_S3_USE_SSL = False
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = 'public-read'

# Static files settings
STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
]

# Simplified settings for collectstatic
DEBUG = False
ALLOWED_HOSTS = ['*']
