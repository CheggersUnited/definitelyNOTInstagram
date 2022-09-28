from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required, current_identity
from App.controllers import auth
from App.models import User

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return redirect('/login')

@index_views.route('/login', methods=['GET'])
def login():
    data = request.values
    data = data.to_dict()
    user = auth.authenticate(data['username'], data['password'])
    print(user.toDict())
    return user.toDict()
    
