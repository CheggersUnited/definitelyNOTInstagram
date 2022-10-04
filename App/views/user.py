from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import current_identity, jwt_required

from App.controllers import (
    create_user,
    delete_user, 
    update_user,
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

@user_views.route('/delete', methods=['GET'])
@jwt_required()
def delete_my_profile():
    return delete_user(current_identity.id)

@user_views.route('/update', methods=['POST'])
@jwt_required()
def update_profile_picture():
    data = request.get_json()
    if data:
        return update_user(current_identity.id, data['image'])
    return {'error': 'Unsuccessful update'}

@user_views.route('/reset', methods=['GET'])
def reset():
    reset_users()
    return "Users reset"