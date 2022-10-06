from App.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Rating(db.Model):
    __tablename__ = "rating"
    id = db.Column('id', db.Integer, primary_key=True)
    uid = db.Column('uid', db.Integer, ForeignKey('user.id'))
    pid = db.Column('pid', db.Integer, ForeignKey('picture.pid'))
    rating = db.Column('rating', db.Boolean, nullable=False)

    def __init__(self, uid, pid, rating):
        self.uid = uid
        self.pid = pid
        self.rating = rating

    def toDict(self):
        return {
            'id': self.id,
            'uid': self.uid,
            'pid': self.pid,
            'rating': self.rating,
            'picture': self.picture.url,
            'username': self.user.username 
        }