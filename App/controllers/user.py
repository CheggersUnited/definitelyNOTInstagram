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

def get_user(username):
    return User.query.filter_by(username=username).first()

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
    return random.shuffle(users)

def get_ranked_users():
    users = User.query.all().order_by(User.points)
    return users

def update_views(username):
    user = User.query.get(username=username)
    if user.views < user.limit:
        user.views += 1
        db.session.commit()
        return True
    return False

def like_or_dislike(user):
    return update_views(user.username) 