from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc 
import random

def get_all_users():
    users = User.query.all()
    return users

def get_all_users_json():
    users = User.query.all()
    return [user.toDict() for user in users]

def get_user(id):
    return User.query.filter_by(id=id).first()

def create_user(username, password, email, image):
    newuser = User(username=username, password=password, email=email, image=image)
    # try:
    db.session.add(newuser)
    db.session.commit()
    return True
    # except IntegrityError:
    #     return False

def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'user successfully deleted'
    return 'user not found'

def update_user(id, image):
    user = User.query.filter_by(id=id).first()
    if user:
        user.image = image
        db.session.add(user)
        db.session.commit()
        return 'image successfully updated'
    return 'user not found'
    
def get_rand_users(id):
    users = User.query.filter(User.distribution < User.limit).filter(User.id != id).all()
    if len(users) < 20:
        users = random.sample(users, len(users))
    else:
        users = random.sample(users, 20)
    for user in users:
        user.distribution += 1
    db.session.commit()
    return [user.toDict() for user in users]

def get_ranked_users():
    users = User.query.order_by(User.points.desc()).all()
    return [user.toDict() for user in users]

def update_views(id):
    user = User.query.filter_by(id=id).first()
    if user.views < user.limit:
        user.views += 1
        db.session.commit()
        return True
    return False

def reset_users():
    users = get_all_users()
    for user in users:
        user.views = 0
        user.points = 0
        user.limit = 5
        user.distribution = 0
    db.session.commit()
    return