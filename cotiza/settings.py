# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime




BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(w1tm8n($1*j^opg9##+cv)qo=uu^e6-0flaw1dk6fsubepnrh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

MEDIA_ROOT = os.path.join(PROJECT_PATH, '/var/www/html/')

MEDIA_URL = '/var/www/html/'


STATICFILES_DIRS = (
    
    os.path.join(BASE_DIR, "static"),)

MEDIA_URL = '/var/www/html/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


INSTALLED_APPS = (
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cotizar',
)



MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = 'cotiza.urls'

WSGI_APPLICATION = 'cotiza.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'cotizador',
#         'USER': 'root',
#         'PASSWORD': 'h3rm3$d4t4b4$3*',
#         'HOST': '104.236.232.222', 
#         'PORT': '3306',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'coti',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': '127.0.0.1', 
        'PORT': '3306',
    }
}


EMAIL_HOST = 'mail.hermes.pe'
EMAIL_HOST_USER = 'cotiza@hermes.pe'
EMAIL_HOST_PASSWORD = 'cotizahermes'
EMAIL_PORT = 25
EMAIL_USE_TLS = True



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=30000)