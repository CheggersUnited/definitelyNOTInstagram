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

def user_profile_create(form):
    done = create_user(form["username"],form["password"],form["email"], form["image"])
    return done   

def get_rand_users():
    users = User.query.all()
    users = random.sample(users, len(users))
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
    db.session.commit()
    return