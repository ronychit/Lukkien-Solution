from .base import *
from dj_database_url import parse as dburl

DEBUG = False

ALLOWED_HOSTS = ['lukkien.herokuapp.com','127.0.0.1',]

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }