import os

class Config(object):
    DEBUG = False
    TESTING = False
    # Update the string below ( scheduled to be broken into environment variables )
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('SECRET_KEY')

class Development(Config):
    DEBUG = True


class Production(Config):
    pass


class Testing(Config):
    TESTING = True