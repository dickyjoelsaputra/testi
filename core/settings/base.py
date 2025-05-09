import os
from dotenv import load_dotenv
load_dotenv()

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    # Minio
    "storages",
    # main
    "product",
    "about_us",
    "contact_us",
    "home",
    "search",
    "blog",
    "global_setting",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # debug mode
    'django_extensions',
    
    # settings
    "wagtail.contrib.settings",
    "django_select2",
    "captcha",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "django.middleware.gzip.GZipMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
                
                
                'global_setting.context_processors.social_context',
                'global_setting.context_processors.global_seo_context',
                'global_setting.context_processors.breadcrump_context',
                'global_setting.context_processors.footer_text_context',
                'global_setting.context_processors.company_profile_context',
                
                'product.context_processors.product_categories_context',
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {        
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'eveza_db'),
        'USER': os.environ.get('DB_USER' , 'dikjul'),
        'PASSWORD': os.environ.get('DB_PASSWORD' , '3225501'),
        'HOST': os.environ.get('DB_HOST' , '103.150.92.204'),
        'PORT': os.environ.get('DB_PORT' , '5432'),
        'CONN_MAX_AGE': 600,  # Tambahkan parameter connection
        'OPTIONS': {
            'sslmode': 'disable',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# ENVIRONMENT = os.getenv("DJANGO_ENV")
# print(f"BASE_DIR: {BASE_DIR}")
# print(f"PROJECT_DIR: {PROJECT_DIR}")
# print(f"ENVIRONMENT: {ENVIRONMENT}")



# MinIO Configuration
AWS_ACCESS_KEY_ID = os.environ.get('MINIO_ACCESS_KEY', 'Mc0s9YnLN6uJZgJoj014')
AWS_SECRET_ACCESS_KEY = os.environ.get('MINIO_SECRET_KEY', 'Xc253mVXdve9wtOexlwRnULJI9Mgr9QSSKlHmpTH')
AWS_STORAGE_BUCKET_NAME = os.environ.get('MINIO_BUCKET_NAME', 'eveza-bucket')
AWS_S3_ENDPOINT_URL = os.environ.get('MINIO_ENDPOINT', 'https://minio-api.eveza.id')
AWS_S3_ADDRESSING_STYLE = "path"
AWS_S3_USE_SSL = True
AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None
AWS_IS_GZIPPED = True
AWS_S3_FILE_OVERWRITE=False


ENVIRONMENT = os.getenv("DJANGO_ENV")
print(f"ENVIRONMENT: {ENVIRONMENT}")

if ENVIRONMENT == "development":
    # Static lokal
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "core", "static"),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "core", "staticfiles")

    # Media tetap MinIO
    MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "location": "media",
                "default_acl": "public-read",
                "file_overwrite": False
            }
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        }
    }
    
    DEBUG = True
else:
    
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "core", "static"),
    ]
        
    # Static dan media semua ke MinIO
    STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/"
    MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "location": "media",
                "default_acl": "public-read",
                "file_overwrite": False
            }
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "location": "static",
                "default_acl": "public-read"
            }
        }
    }
    
    DEBUG = False

# Django sets a maximum of 1000 fields per form by default, but particularly complex page models
# can exceed this limit within Wagtail's page editor.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000


# Wagtail settings

WAGTAIL_SITE_NAME = "core"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = ['csv', 'docx', 'key', 'odt', 'pdf', 'pptx', 'rtf', 'txt', 'xlsx', 'zip']



CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    },
    "select2": {
        # "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        # "LOCATION": "127.0.0.1:11211",
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = "select2"
# SELECT2_JS = ['django_select2/django_select2.js']
# SELECT2_CSS = ['django_select2/django_select2.css']

# CAPTCHA Configuration
CAPTCHA_FONT_SIZE = 40
CAPTCHA_LENGTH = 6
CAPTCHA_TIMEOUT = 5  # minutes

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'dickyjoelsaputra@gmail.com')


WAGTAILIMAGES_EXTENSIONS = ["gif", "jpg", "jpeg", "png", "webp", "svg"]
WAGTAILEMBEDS_RESPONSIVE_HTML = True
# WAGTAILEMBEDS_FINDERS = [
#     {
#         'class': 'wagtail.embeds.finders.oembed'
#     }
# ]