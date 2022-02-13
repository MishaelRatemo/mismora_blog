from flask import Flask
from config import config_options

from flask_sqlalchemy import SQLAlchemy

# database initialization
db = SQLAlchemy()



def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    
    #flask extensions initialization
    db.init_app(app)
    
    #  registration  of Blueprint
    from .main import  root as app_blueprint
    app.register_blueprint(app_blueprint)
    
    return app 
     