from .common import *

SECRET_KEY = 'development-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://hellodjango_blog_ydm_elasticsearch_local:9200/'
