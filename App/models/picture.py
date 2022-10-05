from App.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Picture(db.Model):
    __tablename__ = "picture"
    pid = db.Column('pid', db.Integer, primary_key=True)
    uid = db.Column('uid', db.Integer, ForeignKey('user.id'))
    url = db.Column('url', db.String(60), nullable=False)
    points = db.Column('points', db.Integer, nullable=False)
    likes = db.Column('likes', db.Integer, nullable=False)
    dislikes = db.Column('dislikes', db.Integer, nullable=False)
    distribution = db.Column('distribution', db.Integer, nullable=False)
    ratings = db.relationship('Rating', backref='picture', lazy='dynamic')

    def __init__(self, uid, url):
        self.uid = uid
        self.url = url
        self.points = 0
        self.likes = 0
        self.dislikes = 0
        self.distribution = 0

    def toDict(self):
        return {
            'pid': self.pid,
            'uid': self.uid,
            'url': self.url,
            'likes': self.likes,
            'dislikes': self.dislikes,
            'points': self.points,
            'distribution': self.distribution,
            'username': self.user.username
        }