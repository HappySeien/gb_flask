import os
from dotenv import load_dotenv


class Config:
    _basedir = os.path.abspath(os.path.dirname(__file__))

    DOTENV_PATH = os.path.join(_basedir, '.env')

    if os.path.exists(DOTENV_PATH):
        load_dotenv(dotenv_path=DOTENV_PATH)

    DEBUG = os.getenv('DEBUG')

    ADMINS = frozenset(os.getenv('ADMINS'))
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_migrations')
    DATABASE_CONNECT_OPTIONS = {}

    WTF_CSRF_ENABLED = True

    FLASK_ADMIN_SWATCH = 'cosmo'

    OPENAPI_URL_PREFIX = '/api/docs'
    OPENAPI_VERSION = '3.0.0'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.51.1'
    