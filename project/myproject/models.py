from myproject import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    profile_pic = db.Column(db.String(64), default='default.jpg')
    employee = db.Column(db.Boolean, nullable=False)
    gender = db.Column(db.String(6))
    address_street = db.Column(db.String(20))
    address_city = db.Column(db.String(10))
    address_province = db.Column(db.String(15))

    Jobs = db.relationship('Jobs', backref='author', lazy=True)

    def __init__(self, email, username, password, type):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        type= type

    def check_password(self, field):
        return check_password_hash(self.password, field)

class Jobs(db.Model):
    __tabelname__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text)
    images = db.Column(db.Text)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comments_on_the_post = db.relationship('comments', backref='comments_on', lazy=True)

    def __init__(self, text, title, images, user_id):
        self.text = text
        self.title = title
        self.images = images
        self.user_id = user_id
