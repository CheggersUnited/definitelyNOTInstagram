from App.models import Rating
from App.database import db

def get_rating(id):
    return Rating.query.filter_by(id=id).first()

def add_rating(uid, pid, rating):
    rating = Rating(uid=uid, pid=pid, rating=rating)
    db.session.add(rating)
    db.session.commit()
    return rating

def delete_rating(id):
    rating = get_rating(id)
    if rating:
        db.session.delete(rating)
        db.session.commit()
        return {"Message": "Rating was successfully deleted"}
    return {"Error": "Invalid rating specified"}

def update_rating(id, rating):
    rating_obj = get_rating(id)
    if rating_obj:
        rating_obj.rating = rating
        db.session.add(rating_obj)
        db.session.commit()
        return rating_obj
    return None

def get_likes(picture):
    likes = picture.ratings.filter(Rating.rating == True).all()
    return likes

def get_dislikes(picture):
    dislikes = picture.ratings.filter(Rating.rating == False).all()
    return dislikes
