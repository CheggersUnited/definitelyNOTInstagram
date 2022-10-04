from App.database import db
from sqlalchemy import ForeignKey, relationship

class Rating(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    uid = db.Column('uid', db.Integer, ForeignKey('user.id'))
    pid = db.Column('pid', db.Integer, ForeignKey('picture.pid'))
    pro_id = db.Column('pro_id', db.Integer, )
    rating = db.Column('rating', db.Boolean, nullable=True)

    def __init__(self, uid, pid, pro_id, rating):
        self.uid = uid
        self.pid = pid
        self.pro_id = pro_id
        self.rating = rating

    def toDict(self):
        return {
            'id': self.id,
            'uid': self.uid,
            'pid': self.pid,
            'pro_id': self.pro_id,
            'rating': self.rating,
            'picture': self.picture.url,
            'username': self.user.username 
        }