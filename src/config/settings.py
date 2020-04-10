"""
Django settings for sklad project.
"""

import os
import datetime

SECRET_KEY = '-e*5j(=#emwya@c+j6%g&pl-bv)g78ui+s@gv=rpi51f-abw@@'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WSGI_APPLICATION = 'config.wsgi.application'
SITE_ID = 1
BACK_END_ID = 1
MAX_UPLOAD_SIZE = 5242880
# System administrators
ADMINS = [('Jakub Mana', 'jakub.mana@trailslah.com')]


# Security

CSRF_COOKIE_AGE = 31449600  # seconds
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = False
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
CSRF_TRUSTED_ORIGINS = []

SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = 0

SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_SECURE = False
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True #  custom nastavenie v loginview
SESSION_COOKIE_DOMAIN = None

LOGOUT_DELETE_COOKIES = [
    # SESSION_COOKIE_NAME,
    'personal_settings',
    'logged',
]

# Django Content Security Policy - 3rd party
# https://django-csp.readthedocs.io/en/latest/index.html
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = None
CSP_IMG_SRC = None
CSP_MEDIA_SRC = None
CSP_FONT_SRC = None
CSP_CONNECT_SRC = None
CSP_STYLE_SRC = None


# Routing
ROOT_URLCONF = 'config.urls_tenants'
PUBLIC_SCHEMA_URLCONF = 'config.urls_public'
APPEND_SLASH = True

LOGIN_URL = 'account:login'
LOGOUT_REDIRECT_URL = 'account:login'
PASSWORD_RESET_TIMEOUT_DAYS = 1
LOGIN_REDIRECT_URL = 'account:branchselect'

# Cache
KEY_PREFIX = ''
TIMEOUT = 300  # seconds

USER_ONLINE_TIMEOUT = 300
USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7


# Database
DATABASE_ROUTERS = ['tenant_schemas.routers.TenantSyncRouter',]



# Files
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # bytes
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]


# Localization & Internationalization
USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_ZONE = 'UTC'
DATE_FORMAT = 'N j, Y'
DATETIME_FORMAT = 'N j, Y, P'
LANGUAGE_CODE = 'sk-SK'
DEFAULT_CHARSET = 'utf-8'
SHORT_DATE_FORMAT = 'm/d/Y'
SHORT_DATETIME_FORMAT = 'm/d/Y P'
TIME_FORMAT = 'P'

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('sk', _('Slovak')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

FIRST_DAY_OF_WEEK = 1



# Middleware
MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'csp.middleware.CSPMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'modules.profile_page.activeuser_middleware.ActiveUserMiddleware',
]


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'config.jinja2_bridge.environment',
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates/html"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
TEMPLATE_URL = os.path.join(BASE_DIR, "templates")


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/assets/'
STATIC_ROOT = '/usr/src/app/static/assets/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static", "libs"),
    os.path.join(BASE_DIR, "static", "media"),
    os.path.join(BASE_DIR, "static", "theme")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/usr/src/app/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'


# Auth
AUTH_USER_MODEL = 'account.User'
TENANT_MODEL = 'account.Account'
GUARDIAN_MONKEY_PATCH = False
PASSWORD_RESET_TIMEOUT_DAYS = 1
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


# Application definition
SHARED_APPS = [
    'tenant_schemas',
    
    'modules.shared_lists',
    'modules.account',
    'modules.lists',
    
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'debug_toolbar',
]

TENANT_APPS = [
    'modules.settings',
    'modules.address_book',
    'modules.dashboard',
    'modules.lists',
    'modules.profile_page',
    'modules.branches',
    'modules.articles',
    'modules.warehouse',

    'django.contrib.contenttypes',

    'django_extensions',
    'debug_toolbar',
]

INSTALLED_APPS = [
    'tenant_schemas',

    'modules.settings',
    'modules.address_book',
    'modules.dashboard',
    'modules.shared_lists',
    'modules.lists',
    'modules.account',
    'modules.redirections',
    'modules.layout.datatables',
    'modules.layout.mainboard',
    'modules.profile_page',
    'modules.branches',
    'modules.articles',
    'modules.warehouse',

    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_datatables',
    'django_select2',

    'django_extensions',
    'debug_toolbar',
]




REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissions'
    ],

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework_datatables.filters.DatatablesFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 25,
    'DATETIME_FORMAT': "%d.%m.%Y | %H:%M",
    'DATE_FORMAT': "%d.%m.%Y",
}


DEBUG = True

FRONT_END_DOMAIN = os.environ.get("DOMAIN")
ALLOWED_HOSTS = ['localhost', 'app', '0.0.0.0', '127.0.0.1', os.environ.get("DOMAIN")]
CUSTOM_REDIRECT_VALUE = [7, 17]
SESSION_COOKIE_DOMAIN = '.' + FRONT_END_DOMAIN
    
# Database
DATABASES = {
    "default": {
        "ENGINE": 'tenant_schemas.postgresql_backend',
        "NAME": 'eqini_core',
        "USER": 'system_handler',
        "PASSWORD": 'hje((*%518dgvrt+*^',
        "HOST": '127.0.0.1',
        "PORT": '5432',
    }
}
