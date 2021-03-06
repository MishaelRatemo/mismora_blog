from flask import Flask
from flask_login import LoginManager
from config import config_options

from flask_sqlalchemy import SQLAlchemy
from flask_mail  import  Mail

from flask_bootstrap import Bootstrap



# database initialization
db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view ='auth.login'

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    
    #flask extensions initialization
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    
    
    #  registration  of Blueprint
    from .main import  root as app_blueprint
    app.register_blueprint(app_blueprint)
    from .auth import auth as app_blueprint
    app.register_blueprint(app_blueprint)
    
    
    return app 
     