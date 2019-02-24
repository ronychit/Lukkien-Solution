from .base import *
from dj_database_url import parse as dburl

DEBUG = True

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'test_db.sqlite3')

DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }