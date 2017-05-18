import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # DEBUG = True
    # DEBUG_TB_INTERCEPT_REDIRECTS = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '4H8#kdJJ22[;2jS)]'
    WTF_CSRF_ENABLED = True

    # email server
    MAIL_SERVER = 'smtp.sparkpostmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USERNAME = 'SMTP_Injection'
    MAIL_PASSWORD = '48db7945541433dba821b68790fa034fd12f8ab3'
    # administrator list
    ADMINS = ['accounts@dallasmakerspace.org'] # email from address


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
