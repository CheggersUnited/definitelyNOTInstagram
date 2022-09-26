from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

def get_all_users():
    users = Profile.query.all()
    return users

def get_user(username):
    return User.query.filter_by(username=username).first()

def create_user(username, password, email):
    newuser = User(username=username, password=password, email=email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return True
    except IntegrityError:
        return False

def user_profile_create(form,filename):
    done = create_user(form["username"],form["password"],form["email"])
    return done   

def get_rand_users():
    pass