from App.models import Picture
from App.database import db
from App.controllers.rating import add_rating
from App.controllers.tiers import *
from App.controllers.user import get_user
import random

def get_picture(pid):
    return Picture.query.filter_by(pid=pid).first()

def add_picture(uid, url):
    picture = Picture(uid=uid, url=url)
    user = get_user(uid)
    if len(user.pictures.all()) < 5:
        db.session.add(picture)
        db.session.commit()
        return "Picture added to {}'s profile".format(picture.user.username)
    return 'Unable to add any more pictures. Limit reached.'

def delete_picture(pid):
    picture = get_picture(pid)
    if picture:
        db.session.delete(picture)
        db.session.commit()
        return 'Picture was successfully removed'
    return 'Invalid picture selected'

def like_a_pic(uid, pid):
    rating = add_rating(uid, pid, True)
    rating.picture.points += 1
    rating.picture.likes += 1
    rating.picture.user.points += 1
    interact(rating.user.id)
    tier_update(rating.picture.user)
    db.session.commit()
    return True
    

def dislike_a_pic(uid, pid):
    rating = add_rating(uid, pid, False)
    interact(rating.user.id)
    rating.picture.dislikes += 1
    if (rating.picture.points - 0.5) > 0:
        rating.picture.points -= 0.5
    if (rating.picture.user.points - 0.5) > 0:
        rating.picture.user.points -= 0.5
        tier_update(rating.picture.user)
    db.session.commit()
    return True

def get_rand_pictures(id):
    pictures = Picture.query.filter(Picture.uid != id)
    pictures = pictures.filter(Picture.distribution < User.limit).all()
    pictures = random.sample(pictures, len(pictures)) if len(pictures) < 50 else random.sample(pictures, 50)
    for pic in pictures:
        pic.distribution += 1
    db.session.commit()
    return pictures