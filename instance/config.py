import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")


class ReleaseConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}
