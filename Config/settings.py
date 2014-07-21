#encoding=utf-8

"""
Django settings for gestioCI project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


'''
1 GLOBAL VARS
2 Application definition
3 Database
4 Custom plugins config
5 Templates
6 Localization
7 EMail
'''


<<<<<<< HEAD
'''
1 Global vars
'''
# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'znh%e(fdnb@haock=go-a+eej*pgt(u=#b_o!0f08v53+rn1j*'
=======
''' 
1 Global vars
'''
# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'sdf%e(ertb@hertk=t&%aEEEj*pgt(u=#b_654f08v53SDe1j*'
>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = [".gestio.cooperativa.cat"]
ROOT_URLCONF = 'Config.urls'
WSGI_APPLICATION = 'Config.wsgi.application'


'''
2 Application definition
'''
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	#gestioCI APPS
    'Invoices', 	# This is gestioCI block1 Selfoccupated coopers APP
<<<<<<< HEAD
	   'Cooper', 		# This is gestioCI block1 Selfoccupated coopers APP
     'General',  # This is the general models APP including five main types of data
=======
	'Cooper', 		# This is gestioCI block1 Selfoccupated coopers APP
>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09
	#common APPS
    'south', 		# This is command line BBDD helper
    'django_cron', 	# This controls scheduled EmailNotifications https://pypi.python.org/pypi/django-cron
    'csvimport', 	# This provides import CSV to Model https://pypi.python.org/pypi/django-csvimport
    'localflavor', 	# This provide NIF/NIE/CIF form field
<<<<<<< HEAD
    'mptt', # This provide Tree management in a 'nested set' style
    #'feincms',
    #'feincms.module.page',
    #'feincms.module.medialibrary'
=======
>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)
TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.tz",
	"django.contrib.messages.context_processors.messages"
)


'''
3 Database
'''
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DEFAULT_INDEX_TABLESPACE = 'indexes'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestioCI',
        'USER' : 'gestioCI',
        'PASSWORD': 'gestioCI',
        'HOST': 'localhost',
    }
}


'''
4 Custom plugins config
'''
#django-csvimport
<<<<<<< HEAD
CSVIMPORT_MODELS = ["Invoices.periodTaxes",
=======
CSVIMPORT_MODELS = ["Invoices.periodTaxes", 
>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09
		"Invoices.SalesInvoices",
		"Invoices.PurchaseInvoices",
		"Invoices.PeriodClose",
		"Invoices.Client",
		"Invoices.Provider",
		"Invoices.period",
		"Invoices.PaymentEntities",
		"Invoices.Coop",
		"Invoices.RefundEntities"]

#django-cron
CRON_CLASSES = [
<<<<<<< HEAD
    "cron.testEmail",
    "cron.EmailsNotifierCron",
    "cron.PeriodCloseAutomaticClose"
]
=======
    "cron.testBot",
    "cron.EmailsNotifierCron",
    "cron.PeriodCloseAutomaticClose"
] 
>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09
CRONJOBS = [
    ('*/1 * * * *', 'Config.cron')
]


'''
5 Templates
'''
# Directory path
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# up and downloadable files
MEDIA_BASE = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_BASE)
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# a) for PRODUCTION
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
# b) for DEVELOPMENT
STATIC_URL = '/static/'
<<<<<<< HEAD
ADMIN_MEDIA_PREFIX = STATIC_ROOT + '/admin/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "templates"),
		BASE_DIR + '/Invoices/templates/',
    BASE_DIR + '/General/templates/',
)


'''
=======
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "templates"),
		BASE_DIR + '/Invoices/templates/',
)


''' 
>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09
6 Localization
'''
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'ca-ES'
LOCALE_PATHS = ( BASE_DIR + "/locale/",)
LANGUAGES = (
		('ca', 'Català'),
		('es', 'Castellano'),
	)
DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = '.'
TIME_ZONE = 'UTC'
USE_L10N = True
USE_I18N = True
USE_TZ = True


'''
7 EMail
'''
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
<<<<<<< HEAD
EMAIL_HOST = "------"
EMAIL_HOST_USER = "------"
EMAIL_HOST_PASSWORD = "------"
DEFAULT_FROM_EMAIL = "------"
=======
EMAIL_HOST = "mail.cooperativaintegral.cat"
EMAIL_HOST_USER = "gestioci@cooperativa.cat" 
EMAIL_HOST_PASSWORD = "0¡salud Y libertad!"
DEFAULT_FROM_EMAIL = "gestioci@cooperativa.cat"
>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09

#Opción 1
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = False

#Opción 2
EMAIL_PORT = 465
EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False

#Opcion3: Nada más que testing
EMAIL_PORT = 25
EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False
<<<<<<< HEAD
=======



>>>>>>> 012c04040d2a54e66042fdc995c35ebfd97a0a09
