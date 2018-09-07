"""
Django settings for chisholm project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ow2%k=p=8^4ncm@&f%djk)06mzvfa+)e8r9*hcdy8_b1q$61v('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.gis',
    'django.contrib.sitemaps'
]

THIRD_PARTY_APPS = [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.settings',
    'wagtail.api.v2',
    'rest_framework',
    'wagtailmenus',
    'wagtailfontawesome',
    'modelcluster',
    'taggit',
    'wagtailgeowidget',
    'condensedinlinepanel'
]

PROJECT_APPS = [
    'seo_page',
    'cms',
    'blog',
    'chisholm',
    'realestate.offices',
    'realestate.agents',
    'realestate.testimonials',
    'realestate.suburbs',
    'realestate.enquiries',
    'realestate.alerts',
    'realestate.careers',
    'realestate.agentbox',  # AgentBox API connection scripts
    'realestate',
    'schools',
    'suburbs_database',
    'inspectre',
    'formbuilder_filefield',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'chisholm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtailmenus.context_processors.wagtailmenus',
                'wagtail.contrib.settings.context_processors.settings',
                'realestate.listings.context_processors.search_listing_form',
                'realestate.listings.context_processors.search_pages'
            ],
        },
    },
]

WSGI_APPLICATION = 'chisholm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

WAGTAIL_SITE_NAME = 'Chisholm & Gamon'

# EMAIL SETTINGS
ANYMAIL = {}
EMAIL_BACKEND = "cms.email_backend.CMSEmailBackend"
FAILOVER_EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_CC = "jason@techequipt.com.au"  # Used by cms.utls.send_email_template
DEFAULT_FROM_EMAIL = 'Chisholm & Gamon Website <noreply@chisholmgamon.com.au>'


GOOGLE_MAPS_V3_APIKEY = ""
GEO_WIDGET_DEFAULT_LOCATION = {'lat': 0.0, 'lng': 0.0}

BLOG_LIMIT_AUTHOR_CHOICES_GROUP = ('Editors',)
BLOG_LIMIT_AUTHOR_CHOICES_ADMIN = True
