from flask_jwt import JWT
from App.models import User

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

def identity(payload):
    return User.query.get(payload['identity'])

def setup_jwt(app):
    return JWT(app, authenticate, identity)