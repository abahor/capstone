from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo, Length

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'enter your email'})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, message='your password is too short')])
    submit = SubmitField('Login')
