from myproject import db, login # , wa
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import abort
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from myproject import app


@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.Straing(64))
    password = db.Column(db.String(128))
    profile_pic = db.Column(db.String(64), default='default.jpg')
    employer = db.Column(db.Boolean, nullable=False)
    male = db.Column(db.Boolean, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address_street = db.Column(db.Text, nullable=False)
    address_city = db.Column(db.String(15), nullable=False)
    address_province = db.Column(db.String(30), nullable=False)
    address_country = db.Column(db.String(15), nullable=False)

    Jobs = db.relationship('Jobs', backref='author', lazy=True)

    def __init__(self, email, username, password, male, address_city, address_street, address_province, address_country,
                 phone_number,
                 type_of_account=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.employer = type_of_account
        self.male = male
        self.phone_number = phone_number
        self.address_street = address_street
        self.address_city = address_city
        self.address_province = address_province
        self.address_country = address_country

    def check_password(self, field):
        return check_password_hash(self.password, field)


class Jobs(db.Model):
    __tablename__ = 'jobs'
    # __searchable__ = ['title', 'text', 'address_of_job']
    __searchable__ = ['address_of_job']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text)
    # images = db.Column(db.Text)
    # coordinates_Latitude = db.Column(db.String(20))
    # coordinates_Longitude = db.Column(db.String(20))
    # address_in_letters = db.Column(db.String(20))
    phone_for_contact = db.Column(db.String(20), nullable=False)
    address_of_job = db.Column(db.Text, nullable=False)
    # address_street = db.Column(db.String(20), nullable=False)
    # address_city = db.Column(db.String(15), nullable=False)
    address_province = db.Column(db.String(30), nullable=False)
    address_country = db.Column(db.String(15), nullable=False)
    applied_for_this_job = db.Column(db.Integer, default=0)

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # comments_on_the_post = db.relationship('comments', backref='comments_on', lazy=True)

    def __init__(self, text, title, user_id, address_province, address_country,
                 phone_number, location):
        self.text = text
        self.title = title
        self.user_id = user_id
        # self.coordinates_Latitude = coordinates_Latitude
        # self.coordinates_Longitude = coordinates_Longitude
        self.phone_for_contact = phone_number
        self.address_of_job = location
        self.address_province = address_province
        self.address_country = address_country


# wa.search_index(app=app, model=Jobs)


# accessible
class MyUsers(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return abort(404)


# accessible
class My_Admin_View(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.email == 'abahormelad@gmail.com':
                return current_user.is_authenticated
        return abort(404)

    def inaccessible_callback(self, name, **kwargs):
        return abort(404)


# ------------- Admin
admin = Admin(app, index_view=My_Admin_View())

admin.add_view(MyUsers(Users, db.session))
admin.add_view(MyUsers(Jobs, db.session))
