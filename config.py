import os

from click import confirmation_option

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/mismorablog'
    
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass
class TestConfig(Config):
    pass
config_options = {
    'development_mode' : DevConfig,
    'production_mode' :ProdConfig,
    'testing' : TestConfig
}