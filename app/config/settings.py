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

DEBUG = True
SECRET_KEY = 'troqueme'
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

URL_PATH_PREFIX = os.environ['URL_PATH_PREFIX'] if 'URL_PATH_PREFIX' in os.environ else 'baggins/'
LOGIN_URL = '/%saccounts/login/' % URL_PATH_PREFIX
LOGIN_REDIRECT_URL = '/%saccounts/profile/' % URL_PATH_PREFIX
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/%sstatic/' % URL_PATH_PREFIX
