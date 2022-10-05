import os
from flask import Flask
from flask_login import LoginManager, current_user
from flask_cors import CORS
from datetime import timedelta


from App.database import create_db

from App.controllers import (
    setup_jwt
)

from App.views import (
    user_views,
    index_views
)

# New views must be imported and added to this list

views = [
    user_views,
    index_views
]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] =  timedelta(minutes=int(os.environ.get('JWT_EXPIRATION_DELTA')))
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
        
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    add_views(app, views)
    create_db(app)
    setup_jwt(app)
    app.app_context().push()
    return app

app = create_app()
