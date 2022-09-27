from models import User
from controllers import user

def like_a_pic(username):
    user = user.get_user(username=username)
    if user.tier == 1:
        user.points += user.tier
    else:
        user.points += (1 - ((user.tier - 1)/10))
    return True


def dislike_a_pic(username):
    user = user.get_user(username=username)
    if (user.points - 0.5) >= 0:
        user.points -= 0.5
    return True
    
def update_limits(user):
        user = User.query.get(username=username)
        if user.tier is not 10:
            user.limit += (user.tier - 1)
        else:
            user.limit = float('inf')
        return True

def tier_update(username):
    user = user.get_user(username=username)
    if(user.points >= 11 and user.points <= 20):
        user.tier = 2
    elif(user.points >= 21 and user.points <= 30):
        user.tier = 3
    elif(user.points >= 31 and user.points <= 40):
        user.tier = 4
    elif(user.points >= 41 and user.points <= 50 ):
        user.tier = 5
    elif(user.points >= 51 and user.points <= 60):
        user.tier = 6
    elif(user.points >= 61 and user.points <= 70):
        user.tier = 7
    elif(user.points >= 71 and user.points <= 80):
        user.tier = 8
    elif(user.points >= 81 and user.points <= 90):
        user.tier = 9
    elif(user.points >= 91 and user.points <= 100):
        user.tier = 10
    return update_limits(user)
