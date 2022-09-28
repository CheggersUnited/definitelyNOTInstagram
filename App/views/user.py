from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_user


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    like_a_pic,
    dislike_a_pic,
    update_limit,
    update_views,
    get_rand_users,
    get_ranked_users,
    get_user,
    user_profile_create,
    like_or_dislike
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

@jwt_required
@user_views.route('/login',methods=['POST'])
def login():
    login_user()

@user_views.route('/loadprofiles', methods=['GET'])
def loadprofiles():
    users = get_rand_users()
    return jsonify(users)

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
    username = current_user.username
    user = get_user(username)
    return jsonify(user)
