from App.models import Rating
from App.database import db

def add_rating(uid, pid, rating):
    rating = Rating(uid=uid, pid=pid, rating=rating)
    db.session.add(rating)
    db.session.commit()
    return 'Rating was submitted'

def delete_rating(id):
    rating = Rating.query.filter_by(id=id).first()
    if rating:
        db.session.delete(rating)
        db.session.commit()
        return 'Rating was successfully deleted'
    return 'Invalid rating specified'

def update_rating(id, rating):
    rating_obj = Rating.query.filter_by(id=id).first()
    if rating_obj:
        rating_obj.rating = rating
        db.session.add(rating_obj)
        db.session.commit()
        return 'Rating updated'
    return 'Invalid rating specified'