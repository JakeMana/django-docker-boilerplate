try:
    from config.settings import *
except ImportError:
    pass



DEBUG = int(os.environ.get("DEBUG", default=0))

FRONT_END_DOMAIN = os.environ.get("DOMAIN")
ALLOWED_HOSTS = ['.' + os.environ.get("DOMAIN"), 'pegas.tpsoft.sk', 'localhost', 'app', '0.0.0.0', '127.0.0.1', 'eqini.sk', 'eqini.eu', '.eqini.sk', '.eqini.eu']
CUSTOM_REDIRECT_VALUE = [7, 17]
SESSION_COOKIE_DOMAIN = '.' + FRONT_END_DOMAIN
PROTOCOL = os.environ.get("PROTOCOL")
PORT = os.environ.get("PORT")
    
# Database
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
    }
}

EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND")
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_FROM")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_TRACK_CLICKS_HTML = False
SENDGRID_TRACK_CLICKS_PLAIN = False


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://' + os.environ.get("REDIS_HOST"),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
