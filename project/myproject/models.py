from myproject import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    profile_pic = db.Column(db.String(64), default='default.jpg')
    employer = db.Column(db.Boolean, nullable=False)
    male = db.Column(db.Boolean, nullable=False)
    address_street = db.Column(db.String(20), nullable=False)
    address_city = db.Column(db.String(15), nullable=False)
    address_province = db.Column(db.String(20), nullable=False)
    address_country = db.Column(db.String(15), nullable=False)

    Jobs = db.relationship('Jobs', backref='author', lazy=True)

    def __init__(self, email, username, password, male, address_city, address_street, address_province, address_country,
                 type_of_account=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.employer = type_of_account
        self.male = male
        self.address_street = address_street
        self.address_city = address_city
        self.address_province = address_province
        self.address_country = address_country

    def check_password(self, field):
        return check_password_hash(self.password, field)


class Jobs(db.Model):
    __tablename__ = 'jobs'
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
