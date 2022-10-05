from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key=True)
    username =  db.Column('username', db.String(60), unique=True, nullable=False)
    password = db.Column('password', db.String(120), nullable=False)
    email = db.Column('email', db.String(60), nullable=False)
    points = db.Column('points', db.Integer, nullable=False)
    tier = db.Column('tier', db.Integer,nullable=False)
    limit = db.Column('limit', db.Integer, nullable=False)
    views = db.Column('views', db.Integer, nullable = False)
    ratings = db.relationship('Rating', backref='user', lazy='dynamic')
    pictures = db.relationship('Picture', backref='user', lazy='dynamic')

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.tier = 1
        self.limit = 5
        self.points = 0
        self.views = 0

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'tier': self.tier,
            'limit': self.limit,
            'points': self.points,
            'pic': self.pictures.first().toDict()
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

