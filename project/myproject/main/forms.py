from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Email, Length


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'enter your email','class':'form-control'})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, message='your password is too short')],
                             render_kw={'placeholder': 'password'})
    submit = SubmitField('Login')


class ResetForm(FlaskForm):
    email = StringField('your email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'your email','class':'form-control'})
    submit = SubmitField('Send reset Email')


class FormRecover(FlaskForm):
    password = PasswordField('The new password', validators=[DataRequired()], render_kw={'placeholder': 'your new '
                                                                                                        'password','class':'form-control'})
    submit = SubmitField('Change')
