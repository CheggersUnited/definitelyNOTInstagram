from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    interact,
    like_a_pic,
    dislike_a_pic,
    update_limit,
    update_views,
    get_rand_users,
    get_ranked_users,
    get_user,
    user_profile_create,
    reset_users
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

# @jwt_required
# @user_views.route('/login',methods=['POST'])
# def login():
#     login_user()

@user_views.route('/loadprofiles', methods=['GET'])
@jwt_required()
def loadprofiles():
    id = current_identity.id
    users = get_rand_users(id)
    return jsonify(users)

@user_views.route('/like/<profile>',methods=['POST'])
@jwt_required()
def like(profile):
    user = current_identity
    profile = get_user(profile)
    if update_views(user.id):
        like_a_pic(profile.username)
        interact(user.username)
    else:
        return {"Error": "Limit Reached"}
    return "{}'s profile has been liked.".format(profile.username)

@user_views.route('/dislike/<profile>',methods=['POST'])
@jwt_required()
def dislike(profile):
    user = current_identity
    profile = get_user(profile)
    if update_views(user.id):
        dislike_a_pic(profile.username)
        interact(user.username)
    else:
        return {"Error": "Limit Reached"}
    return "{}'s profile has been disliked.".format(profile.username)

@user_views.route('/rankings',methods=['GET'])
@jwt_required()
def rankings():
    users = get_ranked_users()
    return jsonify(users)

@user_views.route('/my',methods=['GET'])
@jwt_required()
def show_my_profile():
    user = get_user(current_identity.id)
    return jsonify(user.toDict())

@user_views.route('/reset', methods=['GET'])
def reset():
    reset_users()
    return "Users reset"