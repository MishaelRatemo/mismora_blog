from distutils.debug import DEBUG
import os

from click import confirmation_option

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/mismorablog'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True
    pass
class TestConfig(Config):
    pass
config_options = {
    'development' : DevConfig,
    'production_mode' :ProdConfig,
    'testing' : TestConfig
}