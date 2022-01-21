# config/dev.py

from .default import *
from os.path import join



APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI= 'sqlite:///' + join(BASE_DIR, 'bmeswebapp.db')