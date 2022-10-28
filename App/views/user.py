from flask import Blueprint, jsonify, request
from flask_jwt import current_identity, jwt_required

from App.controllers import (
    create_user,
    delete_user, 
    get_all_users,
    get_all_users_json,
    interact,
    like_a_pic,
    dislike_a_pic,
    get_likes,
    get_dislikes,
    update_limit,
    update_views,
    get_picture,
    add_picture,
    delete_picture,
    get_rand_pictures,
    get_ranked_pictures,
    get_ranked_users,
    get_user,
    reset_users
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

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
    return {"Message": "{}'s picture has been liked.".format(get_picture(pid).user.username)}

@user_views.route('/dislike/<pid>',methods=['POST'])
@jwt_required()
def dislike(pid):
    if update_views(current_identity.id):
        dislike_a_pic(current_identity.id, pid)
    else:
        return {"Error": "Limit Reached"}
    return {"Message": "{}'s picture has been disliked.".format(get_picture(pid).user.username)}

@user_views.route('/rankings/users',methods=['GET'])
@jwt_required()
def ranking_users():
    users = get_ranked_users()
    return jsonify([user.toDict() for user in users])

@user_views.route('/rankings/pictures',methods=['GET'])
@jwt_required()
def ranking_pictures():
    pictures = get_ranked_pictures()
    return jsonify([picture.toDict() for picture in pictures])

@user_views.route('/my',methods=['GET'])
@jwt_required()
def show_my_profile():
    user = get_user(current_identity.id)
    return jsonify(user.toDict())

@user_views.route('/addpic', methods=['POST'])
@jwt_required()
def add_a_picture():
    data = request.get_json()
    return jsonify(add_picture(current_identity.id, data['url']).toDict())
    
@user_views.route('/deletepic/<pid>', methods=['DELETE'])
@jwt_required()
def delete_a_picture(pid):
    return delete_picture(pid)

@user_views.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_my_profile():
    return delete_user(current_identity.id)

@user_views.route('/<pid>/likes', methods=['GET'])
@jwt_required()
def get_picture_likes(pid):
    picture = get_picture(pid)
    likes = get_likes(picture)
    return jsonify([like.toDict() for like in likes])

@user_views.route('/<pid>/dislikes', methods=['GET'])
@jwt_required()
def get_picture_dislikes(pid):
    picture = get_picture(pid)
    dislikes = get_dislikes(picture)
    return jsonify([dislike.toDict() for dislike in dislikes])


# This view is used when testing
@user_views.route('/reset', methods=['GET'])
def reset():
    reset_users()
    return "Users reset"