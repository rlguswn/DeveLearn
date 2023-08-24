"""
Django settings for develearn project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import environ
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default='',)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOWED_ORIGINS = [
# 	# 허용할 Origin 추가
#     "http://127.0.0.1:9000"
# ]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    # Custom App
    'classroom',
    'news',
    'user',
    # For allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.google',
    # For JWT
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # For drf-spectacular
    'drf_spectacular',
]

SPECTACULAR_SETTINGS = {
    # drf-spectacular 라이브러리 version up이 없이도 자신의 원하는 swagger-ui의 version을 사용할수있다.
    # swagger-ui version 정보는 여기서 확인 https://www.npmjs.com/package/swagger-ui
    'SWAGGER_UI_DIST': '//unpkg.com/swagger-ui-dist@3.44.0', 
    'SWAGGER_UI_FAVICON_HREF': '//unpkg.com/swagger-ui-dist@3.44.0/favicon-32x32.png',

    "SWAGGER_UI_SETTINGS": {
        'deepLinking': True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경됩니다. (특정 API url 공유시 유용하기때문에 True설정을 사용합니다)
        'persistAuthorization': True,  # True 이면 SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않습니다.
        'displayOperationId': True,  # True이면 API의 urlId 값을 노출합니다. 대체로 DRF api name둘과 일치하기때문에 api를 찾을때 유용합니다.
        'filter': True,  # True 이면 Swagger UI에서 'Filter by Tag' 검색이 가능합니다.
        # Swagger UI 가 제공하는 UI 커스터마이징 옵션값들입니다. 아래 링크를 보면 어떤 커스터마이징 옵션들이 존재하는지 알수있습니다.
        # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
    },
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'develearn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'develearn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME', default='',),
        'USER': env.str('DB_USER', default='',),
        'PASSWORD': env.str('DB_PASSWORD', default='',),
        'HOST': env.str('DB_HOST', default='',),
        'PORT': env.str('DB_PORT', default='',),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.User"

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id': env.str('KAKAO_CLIENT_ID', default='',),
            'secret': env.str('KAKAO_SECRET_KEY', default='',),
            'key': ''
        },
    },
    'naver': {
        'APP': {
            'client_id': env.str('NAVER_CLIENT_ID', default='',),
            'secret': env.str('NAVER_SECRET_KEY', default='',),
            'key': ''
        },
    },
    'google': {
        'APP': {
            'client_id': env.str('GOOGLE_CLIENT_ID', default='',),
            'secret': env.str('GOOGLE_SECRET_KEY', default='',),
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

ACCOUNT_USER_MODEL_USERNAME_FIELD = "user_id" # 소셜 로그인 USERNAME 필드 설정
#ACCOUNT_AUTHENTICATION_METHOD = 'user_id' # 소셜 로그인 인증 설정
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None # 'none'

SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = False # Post 요청 필요, True 비권장

# 로그인, 로그아웃 리다이렉트 - URL path name 작성
# LOGIN_REDIRECT_URL = 'main'
# ACCOUNT_LOGOUT_REDIRECT_URL = 'main'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY': False, # Default True
    'JWT_AUTH_COOKIE_USE_CSRF' : True,
    'JWT_AUTH_COOKIE': 'develearn-auth-cookie',
    'JWT_AUTH_REFRESH_COOKIE': 'develearn-refresh-token',
    'LOGOUT_ON_PASSWORD_CHANGE' : True,
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}
