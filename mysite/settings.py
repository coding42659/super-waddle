"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
#testing
#testing again.

#CSRF_FAILURE_VIEW = "mysite"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b#s*_o(3t3ai_k(c5po@h7a=nj5#vjkd3u7ckhnx@)mi=8fn67'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#need to define
LOGIN_REDIRECT_URL = '/'
ALLOWED_HOSTS = ["*"]
# '''
import os
# import psycopg2

# conn = psycopg2.connect(os.environ["postgresql://munchy:HNijsJ6xXjqKV4_Ahm-ZYw@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dcalmed-beast-4627"])

# with conn.cursor() as cur:
 #    cur.execute("SELECT now()")
  #   res = cur.fetchall()
   #  conn.commit()
  #   print(res)
# '''
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
     'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
   'django.contrib.sites',
    'testing.apps.TestingConfig',
    #'WebAuthn.apps.WebAuthnConfig',
    'Links.apps.LinksConfig',
    'progress.apps.ProgressConfig',
    'Uploads.apps.UploadsConfig',
    'uploader.apps.UploaderConfig',

  'allauth',
    'allauth.account',
   'allauth.socialaccount',
 'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
  'accountss.apps.AccountssConfig',
  'blog',
  'personal',
  'munchyblog',
  'apps',
  'pages',
  'polls',
  'homepage',
  'a1homepage',
  'rest_framework',
  #'django.contrib.accounts2',

  
   # 'progress.apps.WebsiteIdeasConfig',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
   'main': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfauu6s2p9c2mc', 
        'USER': 'sjndilncqlgysz',
        'PASSWORD': 'e8538d5f8ee333d967cea5ec709d41be8106f14a642dbf270ef43535217c58f6',

        'HOST': 'ec2-34-230-198-12.compute-1.amazonaws.com',
        'PORT': '5432',
    },
  #  'munchy': {
      #  'ENGINE': 'django.db.backends.postgresql',
       # 'NAME': 'munchyteam', 
#        'USER': 'munchyteam_user',
  #      'PASSWORD': 'fFk3CaIEYpw50VzjtQwP0XznZrUViQm6',
  #      'HOST': 'dpg-cc4i6e1gp3jiap6h5rf0-a.ohio-postgres.render.com',
  #      'PORT': '5432',
   # },
    #'garbage': {
    #    'ENGINE': 'django.db.backends.postgresql',
    #    'NAME': 'railway', 
    #    'USER': 'postgres',
    #    'PASSWORD': 'QsWvrljPSwOXhfTZWxMH',
    #    'HOST': 'containers-us-west-30.railway.app',
    #    'PORT': '5776',
    #},
   # 'default-test-2':{
  #      'ENGINE': 'django.db.backends.postgresql',
   #     'NAME': 'yugabyte',
   #     'USER': 'admin',
 #      'PASSWORD': 'Rq44vGwcSsEAzZeHtEdpGtHJayG7cA',
 #      'HOST': 'us-west-2.bb352230-c512-4425-9e64-461fa9f2e31a.aws.ybdb.io',
 #      'PORT': '5433',
       #'CONN_MAX_AGE': None,
 #   },
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'munchysite',
        'USER': 'munchy',
        'PASSWORD': '40jpUUMYoOjWD3yFquNeCbOAtEgbt8',
        'HOST': 'tcp-mo1.mogenius.io',
        'PORT': '36010',
    },
  #          'default2':{
    #    'ENGINE': 'django_cockroachdb',
     #   'NAME': 'defaultdb',
    #    'USER': 'munchy',
    #    'PASSWORD': '40jpUUMYoOjWD3yFquNeCbOAtEgbt8',
   #     'HOST': 'free-tier14.aws-us-east-1.cockroachlabs.cloud',
    #    'PORT': '26257',
     #   'OPTIONS': {
            #'sslmode': 'verify-full',
    #        'options': '--cluster=calmed-beast-4627'
    #    },
       #'CONN_MAX_AGE': None,
    },
    # 'default-test': {
      #   'ENGINE': 'django.db.backends.postgresql',
      # 'NAME': 'yugabyte',
      #  'USER': 'munchy',
     #  'PASSWORD': 'Munchy1234',
    #   'HOST': 'us-west-2.1226948a-6d45-49b7-b41e-1632a207e96b.aws.ybdb.io',
    #   'PORT': '5433',
    
#    }
    #'morestuff': {
    #    default='postgresql://postgres:QsWvrljPSwOXhfTZWxMH@containers-us-west-30.railway.app:5776/railway'
    #}
   
   
    
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
       'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
     },
    {
      'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
   {
        'NAME':      
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    }
]
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
  
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, 'static-collected')

X_FRAME_OPTIONS = '*'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

 )

MEDIA_ROOT = os.path.join(BASE_DIR, '.well-known')#'media'
MEDIA_URL = '.well-known/' #real one - #MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
SITE_ID = 2

SOCIALACCOUNT_PROVIDERS = {

 "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:

        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
       }
   },
    "github": {

      "SCOPE": [
        "user:email"
     ]
  
      }
  
        }



DISABLE_COCKROACHDB_TELEMETRY = True


#Btw im going to try to add discord as a sign in option later [Hudson]




    
