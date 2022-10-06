from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import current_identity, jwt_required

from App.controllers import (
    create_user,
    delete_user, 
    get_all_users,
    get_all_users_json,
    interact,
    like_a_pic,
    dislike_a_pic,
    update_limit,
    update_views,
    get_picture,
    get_rand_pictures,
    get_ranked_pictures,
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

@user_views.route('/loadpictures', methods=['GET'])
@jwt_required()
def loadpics():
    pics = get_rand_pictures(current_identity.id)
    return jsonify([pic.toDict() for pic in pics])

@user_views.route('/like/<pid>',methods=['POST'])
@jwt_required()
def like(pid):
    if update_views(current_identity.id):
        like_a_pic(current_identity.id, pid)
    else:
        return {"Error": "Limit Reached"}
    return "{}'s picture has been liked.".format(get_picture(pid).user.username)

@user_views.route('/dislike/<pid>',methods=['POST'])
@jwt_required()
def dislike(pid):
    if update_views(current_identity.id):
        dislike_a_pic(current_identity.id, pid)
    else:
        return {"Error": "Limit Reached"}
    return "{}'s picture has been disliked.".format(get_picture(pid).user.username)

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