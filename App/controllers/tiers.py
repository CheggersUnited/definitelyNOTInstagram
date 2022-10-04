from App.models import User
from App.database import db

def interact(username):
    user = User.query.filter_by(username=username).first()
    if user.tier == 1:
        user.points += user.tier
    else:
        user.points += (1 - ((user.tier - 1)/10))
    tier_update(username)
    db.session.commit()
    return True

def like_a_pic(username):
    interact(username)
    return True

def dislike_a_pic(username):
    user = User.query.filter_by(username=username).first()
    if (user.points - 0.5) >= 0:
        user.points -= 0.5
        tier_update(username)
        db.session.commit()
    return True

def update_limit(user):
    if (user.tier * 3) < user.limit and user.tier != 1:
            user.limit -= user.tier
    else:
        if user.tier != 10:
            user.limit += (user.tier - 1)
        else:
            user.limit = float('inf')    
    db.session.commit()   
    return True

def tier_update(username):
    user = User.query.filter_by(username=username).first()
    if (user.points % 10) != 0:
        user.tier = int(user.points / 10) + 1
    else:
        user.tier = int(user.points / 10)
    db.session.commit()
    return update_limit(user)
