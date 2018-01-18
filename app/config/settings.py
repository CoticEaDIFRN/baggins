import os

MY_APPS = (
    'tipo',
    'contrato',
    'financeiro',
)

THIRD_APPS = (
    'django_brfied.django_brfied',
    'django_extensions',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS = MY_APPS + THIRD_APPS + DJANGO_APPS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#AUTH_PASSWORD_VALIDATORS = [
#    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
#]


def env_or_default(env_name, default_value):
    return os.environ[env_name] if env_name in os.environ else default_value


LANGUAGE_CODE = env_or_default('DJANGO_LANGUAGE_CODE', 'pt-br')
TIME_ZONE = env_or_default('DJANGO_TIME_ZONE', 'UTC')
USE_I18N = env_or_default('DJANGO_USE_I18N', 'True') == 'True'
USE_L10N = env_or_default('DJANGO_USE_L10N', 'True') == 'True'
USE_TZ = env_or_default('DJANGO_USE_TZ', 'True') == 'True'

DEBUG = env_or_default('DJANGO_DEBUG', 'True') == 'True'
SECRET_KEY = env_or_default('DJANGO_SECRET_KEY', 'troqueme')
ALLOWED_HOSTS = [x for x in env_or_default('DJANGO_SECRET_ALLOWED_HOSTS', '*').split(',')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env_or_default('DJANGO_DB_HOST', 'db'),
        'PORT': int(env_or_default('DJANGO_DB_PORT', '5432'),),
        'NAME': env_or_default('DJANGO_DB_NAME', 'postgres'),
        'USER': env_or_default('DJANGO_DB_USER', 'postgres'),
        'PASSWORD': env_or_default('DJANGO_DB_PASS', 'postgres'),
    }
}

URL_PATH_PREFIX = env_or_default('URL_PATH_PREFIX', 'baggins/')
LOGIN_URL = '/%saccounts/login/' % URL_PATH_PREFIX
LOGIN_REDIRECT_URL = '/%saccounts/profile/' % URL_PATH_PREFIX
STATIC_URL = '/%sstatic/' % URL_PATH_PREFIX
