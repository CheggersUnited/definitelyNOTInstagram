from App.models import User, Picture
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

def create_user(username, password, email):
    newuser = User(username=username, password=password, email=email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except IntegrityError:
        return None

def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return 'User successfully deleted'
    return 'User not found'
    
def get_rand_pictures(id):
    pictures = Picture.query.filter(Picture.uid != id).all()
    pictures = random.sample(pictures, len(pictures)) if len(pictures) < 50 else random.sample(pictures, 50)
    return pictures

def get_ranked_pictures():
    pictures = Picture.query.order_by(Picture.points.desc())
    return pictures

def get_ranked_users():
    users = User.query.order_by(User.points.desc())
    return users

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
    db.session.commit()
    return