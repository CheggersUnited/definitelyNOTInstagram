from App.models import User
from App.database import db
from App.controllers.user import get_user, update_views

def interact(id):
    user = get_user(id)
    if user.tier == 1:
        user.points += user.tier
    else:
        user.points += (1 - ((user.tier - 1)/10))
    db.session.commit()
    tier_update(user)
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

def tier_update(user):
    tier = user.tier
    user.tier = int(user.points / 10) + 1
    if user.tier != tier:
        update_limit(user)
    db.session.commit()
    return True
