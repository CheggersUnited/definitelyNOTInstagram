from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


# @user_views.route('/users', methods=['GET'])
# def get_user_page():
#     users = get_all_users()
#     return render_template('users.html', users=users)

# @user_views.route('/api/users')
# def client_app():
#     users = get_all_users_json()
#     return jsonify(users)

# @user_views.route('/static/users')
# def static_user_page():
#   return send_from_directory('static', 'static-user.html')

@user_views.route('/loadprofiles', methods=['GET'])
def loadprofiles():
    pass

@user_views.route('/profile/like',methods=['POST'])
def like():
    pass

@user_views.route('/profile/dislike',methods=['POST'])
def dislike():
    pass

@user_views.route('/profile/rankings',methods=['GET'])
def rankings():
    pass

@user_views.route('/profile/my',methods=['GET'])
def show_my_profile():
    pass
