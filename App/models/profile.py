from App.database import db

class Profile(db.Model):
    pid = db.Column('pid',db.Integer,primary_key=True)
    uid = db.Column('uid',db.Integer, db.ForeignKey('user.id'),nullable=False)
    first_name = db.Column('first_name',db.String(60),nullable=False)
    last_name = db.Column('last_name',db.String(60),nullable=False)
    rating = db.Column('rating', db.Integer, nullable=False)
    points = db.Column('tier_points', db.Integer, nullable=False)
    tier = db.Column('tier', db.Integer, nullable=False)
    url = db.Column('pro_pic', db.String(200), nullable=True)

    def toDict(self):
        return{
                'pid' :self.pid,
                'uid ':self.uid,
                'first_name' :self.first_name,
                'last_name' :self.last_name,
                'rating': self.rating,
                'tier_points': self.points,
                'tier': self.tier,
                'pro_pic': self.url
            }
