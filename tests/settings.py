import os
import sys

DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'cookies_are_delicious_delicacies'
ROOT_URLCONF = 'urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MIDDLEWARE_CLASSES = ()
DEFAULT_INDEX_TABLESPACE = ''

# Make sure the copy of seeker in the directory above this one is used.
sys.path.insert(0, BASE_DIR)

INSTALLED_APPS = (
    'bungiesearch',
    'core',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

BUNGIESEARCH = {
    'URLS': [os.getenv('ELASTIC_SEARCH_URL', 'localhost')],
    'ES_SETTINGS': {
        'http_auth': os.getenv('ELASTIC_SEARCH_AUTH')
    },
    'ALIASES': {
        'bsearch': 'core.search_aliases'
    },
    'INDICES': {
        'bungiesearch_demo': {
            'models': 'core.search_indices',
            'settings': {
                'number_of_shards': 1,
                'number_of_replicas': 0,
            }
        },
        'bungiesearch_demo_bis': {
            'models': 'core.search_indices_bis',
            'settings': {
                'number_of_shards': 1,
                'number_of_replicas': 0
            }
        }
    },
    'SIGNALS': {
        'BUFFER_SIZE': 1,
        'SIGNAL_CLASS': 'core.bungie_signal.BungieTestSignalProcessor'
    },
    'TIMEOUT': 30
}
