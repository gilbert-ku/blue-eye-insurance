import os

class DevelopmentConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///insurance.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
