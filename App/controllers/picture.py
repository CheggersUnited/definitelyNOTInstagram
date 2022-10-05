from App.models import Picture
from App.database import db
from App.controllers.rating import add_rating
from App.controllers.tiers import *

def get_picture(pid):
    return Picture.query.filter_by(pid=pid).first()

def add_picture(uid, url):
    picture = Picture(uid=uid, url=url)
    if len(picture.user.pictures) < 5:
        db.session.add(picture)
        db.session.commit()
        return "Picture added to {}'s profile".format(picture.user.username)
    return 'Unable to add any more pictures. Limit reached.'

def delete_picture(pid):
    picture = Picture.query.filter_by(pid=pid).first()
    if picture:
        db.session.delete(picture)
        db.session.commit()
        return 'Picture was successfully removed'
    return 'Invalid picture selected'

def like_a_pic(uid, pid):
    rating = add_rating(uid, pid, True)
    rating.picture.points += 1
    interact(rating.user.id)
    db.session.commit()
    return True
    

def dislike_a_pic(uid, pid):
    rating = add_rating(uid, pid, False)
    interact(rating.user.id)
    if (rating.picture.points - 0.5) > 0:
        rating.picture.points -= 0.5
        db.session.commit()
    return True