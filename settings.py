import os
from python_brfied.env import env, env_as_bool, env_as_list, env_as_int


# Development
DEBUG = env_as_bool('DJANGO_DEBUG', True)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}, },
    'loggers': {
        '': {'handlers': ['console'], 'level': 'DEBUG'},
    },
}
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: 'localhost' in request.get_host() or '127.0.0.1' in request.get_host() or 'sso' in request.get_host(),
}

MY_APPS = ('tipo', 'contrato', 'financeiro', )


# Apps
MY_APPS = env_as_list('MY_APPS', 'tipo,contrato,financeiro,django_brfied,ege_utils')
DEV_APPS = env_as_list('DEV_APPS', 'debug_toolbar,django_extensions' if DEBUG else '')
THIRD_APPS = env_as_list('THIRD_APPS', 'rest_framework')
DJANGO_APPS = env_as_list('DJANGO_APPS',
                          'django.contrib.admin,'
                          'django.contrib.auth,'
                          'django.contrib.contenttypes,'
                          'django.contrib.sessions,'
                          'django.contrib.messages,'
                          'django.contrib.staticfiles')
INSTALLED_APPS = MY_APPS + THIRD_APPS + DEV_APPS + DJANGO_APPS


# Middleware
MIDDLEWARE = env_as_list('MIDDLEWARE', 'django.middleware.security.SecurityMiddleware,'
                                       'django.contrib.sessions.middleware.SessionMiddleware,'
                                       'django.middleware.common.CommonMiddleware,'
                                       'django.middleware.csrf.CsrfViewMiddleware,'
                                       'django.contrib.auth.middleware.AuthenticationMiddleware,'
                                       'django.contrib.messages.middleware.MessageMiddleware,'
                                       'django.middleware.clickjacking.XFrameOptionsMiddleware')
if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# Template engine
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'ege_utils.context_processors.ege',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'HOST': env('POSTGRES_HOST', 'db'),
        'PORT': env('POSTGRES_PORT', '5432'),
        'NAME': env('POSTGRES_DB_BAGGINS', 'ege_baggins'),
        'USER': env('POSTGRES_USER', 'postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', 'postgres'),
    }
}


# Routing
WSGI_APPLICATION = env('DJANGO_WSGI_APPLICATION', 'wsgi.application')
ALLOWED_HOSTS = env_as_list('DJANGO_ALLOWED_HOSTS', '*' if DEBUG else '')
USE_X_FORWARDED_HOST = True
ROOT_URLCONF = env('DJANGO_ROOT_URLCONF', 'urls')
URL_PATH_PREFIX = env('URL_PATH_PREFIX', 'ege/bolsistas/')
STATIC_URL = env('DJANGO_STATIC_URL', "/%s%s" % (URL_PATH_PREFIX, 'static/'))
STATIC_ROOT = "/static"


# Localization
LANGUAGE_CODE = env('DJANGO_USE_I18N', 'pt-br')
TIME_ZONE = env('DJANGO_USE_I18N', 'UTC')
USE_I18N = env_as_bool('DJANGO_USE_I18N', True)
USE_L10N = env_as_bool('DJANGO_USE_L10N', True)
USE_TZ = env_as_bool('DJANGO_USE_TZ', True)
DATE_FORMAT = env('DJANGO_DATE_FORMAT', 'd/b/Y')
SHORT_DATE_FORMAT = env('DJANGO_SHORT_DATE_FORMAT', 'd/m/Y')


# Auth and Security... some another points impact on security, take care!
SECRET_KEY = env('DJANGO_SECRET_KEY', 'changeme')
LOGIN_URL = env("DJANGO_LOGIN_URL", 'http://localhost/ege/bolsistas/jwt/login')
LOGOUT_URL = env("DJANGO_LOGOUT_URL", 'http://localhost/ege/bolsistas/logout/')
LOGIN_REDIRECT_URL = env("DJANGO_LOGIN_REDIRECT_URL", 'http://localhost/ege/bolsistas/')
LOGOUT_REDIRECT_URL = env("DJANGO_LOGOUT_REDIRECT_URL", 'http://localhost/ege/bolsistas/')
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
EGE_ACESSO_JWT_AUTHORIZE = env("EGE_ACESSO_JWT_AUTHORIZE", 'http://localhost/ege/acesso/jwt/authorize/')
EGE_ACESSO_JWT_VALIDATE = env("EGE_ACESSO_JWT_VALIDATE", 'http://acesso:8000/ege/acesso/jwt/validate/')
EGE_ACESSO_JWT_LOGOUT = env("EGE_ACESSO_JWT_LOGOUT", 'http://acesso:8000/ege/acesso/logout/')
EGE_ACESSO_JWT_CLIENT_ID = env("EGE_ACESSO_JWT_CLIENT_ID", '_EGE_ACESSO_JWT_CLIENT_ID_')
EGE_ACESSO_JWT_SECRET = env("EGE_ACESSO_JWT_SECRET", '_EGE_ACESSO_JWT_SECRET_')
# EGE_UTILS_AUTH_JWT_BACKEND = env("EGE_UTILS_AUTH_JWT_BACKEND", 'ege_utils.backends.CreateNewUserJwtBackend')
EGE_UTILS_AUTH_JWT_BACKEND = env("EGE_UTILS_AUTH_JWT_BACKEND", 'contrato.backends.CreateNewUserJwtBackend')
# AUTH_USER_MODEL = env("DJANGO_AUTH_USER_MODEL", 'ege_bolsistas.Profile')

# Session
SESSION_CACHE_ALIAS = env('DJANGO_SESSION_CACHE_ALIAS', 'default')
SESSION_COOKIE_AGE = env_as_int('DJANGO_SESSION_COOKIE_AGE', 1209600)
SESSION_COOKIE_DOMAIN = env('DJANGO_SESSION_COOKIE_DOMAIN', None)
SESSION_COOKIE_HTTPONLY = env_as_bool('DJANGO_SESSION_COOKIE_HTTPONLY', True)
SESSION_COOKIE_NAME = env('DJANGO_SESSION_COOKIE_NAME', 'egessosessionid')
SESSION_COOKIE_PATH = env('DJANGO_SESSION_COOKIE_PATH', '/%s' % URL_PATH_PREFIX)
SESSION_COOKIE_SAMESITE = env('DJANGO_SESSION_COOKIE_SAMESITE', 'Strict')
SESSION_COOKIE_SECURE = env_as_bool('DJANGO_SESSION_COOKIE_SECURE', False)

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'ege_utils.authentication.SecretDelegateAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    # 'DEFAULT_FILTER_BACKENDS': 'cnes.apiutils.APIFilterBackend',
}

SECURE_PROXY_SSL_HEADER = env_as_list('DJANGO_SECURE_PROXY_SSL_HEADER', 'HTTP_X_FORWARDED_PROTO,https')
