from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = True
ALLOWED_HOSTS = ['82.156.109.20', 'www.yaodianmi.top', 'blog.yaodianmi.top']

HAYSTACK_CONNECTIONS['default']['URL'] = 'http://hellodjango_blog_ydm_elasticsearch:9200/'