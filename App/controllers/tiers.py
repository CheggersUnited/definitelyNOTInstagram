from models import User
from App.controllers import user
from App.database import db

def like_a_pic(username):
    user = user.get_user(username=username)
    if user.tier == 1:
        user.points += user.tier
    else:
        user.points += (1 - ((user.tier - 1)/10))
    db.session.commit()
    return True


def dislike_a_pic(username):
    user = user.get_user(username=username)
    if (user.points - 0.5) >= 0:
        user.points -= 0.5
        db.session.commit()
    return True
    
def update_limits(user):
        user = User.query.get(username=username)
        if user.tier is not 10:
            user.limit += (user.tier - 1)
        else:
            user.limit = float('inf')
        db.session.commit()   
        return True
        

def tier_update(username):
    user = user.get_user(username=username)
    if (user.points % 10) != 0:
        user.tier = int(user.points / 10) + 1
    else:
        user.tier = int(user.points / 10)
    db.session.commit()
    return update_limits(user)
