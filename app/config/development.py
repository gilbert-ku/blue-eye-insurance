import os
import datetime
class DevelopmentConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///insurance.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # jwt token expiration time set to 2 hrs
    JWT_EXPIRATION_DELTA = datetime.timedelta(hours=2)
    JWT_TOKEN_LOCATION = ["headers"]
    DEBUG = True
