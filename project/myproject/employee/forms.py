from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo, Length


class Register(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'enter your email'})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, message='your password is too short')],
                             render_kw={'placeholder': 'Password'})
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password', message
    ='Password must match')], render_kw={
        'placeholder': 'Retype password'})
    street = StringField('street', validators=[DataRequired()], render_kw={'placeholder': 'street'})
    city = StringField('City', validators=[DataRequired()], render_kw={'placeholder': 'City'})
    province = SelectField('State', validators=[DataRequired()], choices=[('assuit', 'assuit'), ('aswan', 'aswan'), (
        'monufia', 'mounifia')])  # ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax
    country = SelectField('Country', validators=[DataRequired()],
                          choices=[('Eg', 'Egypt'), ('Jo', 'Jorden'), ('Sa', 'Saudi')])
    submit = SubmitField('Register')


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'enter your email'})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, message='your password is too short')])
    submit = SubmitField('Login')


class resetForm():
    email = StringField('your email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'your email'})
    submit = SubmitField('Send reset Email')
