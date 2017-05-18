import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '4H8#kdJJ22[;2jS)]'
    WTF_CSRF_ENABLED = True

    # email server
    MAIL_SERVER = 'smtp.webfaction.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USERNAME = 'voucher_britton'
    MAIL_PASSWORD = 'paperless!123'
    # administrator list
    ADMINS = ['dms@smarterwebapps.com']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
