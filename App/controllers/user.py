from App.models import User,Profile
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

def create_profile(email,profile_data):
    try:
        user = User.query.filter_by(email = email).first()
        profile = Profile(
                uid = user.id,
                first_name = profile_data['first_name'],
                last_name = profile_data['last_name'],
                rating = 0, # rating, points are preset to 0
                points = 0,
                tier = 1, # all users start at tier 1
                url = profile_data['url']       
        )
        db.session.add(profile)
        db.session.commit()
        return True
    except(Exception):
        # User.query.filter_by(email = email).delete()
        # db.session.commit()
        print ("User not found")
        return False


# Have to review below code

# def user_profile_create(form,filename):
#     done = create_user(form["username"],form["password"],form["email"])
    
#     if done:
#         y = create_profile(form['email'],form,filename)
        
#         if y:
#             return True
#         else:
#             return False
#     else:
#         return False    
