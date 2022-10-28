from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required
from App.controllers import auth
from App.controllers.user import create_user
from App.models import User


index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')
    
@index_views.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if data:
        return create_user(data['username'], data['password'], data['email']).toDict()
    return {"Error": "Unsuccessful creation"}
