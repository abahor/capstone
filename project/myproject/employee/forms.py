from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'enter your email'})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, message='your password is too short')],
                             render_kw={'placeholder': 'Password'})
    pass_confirm = PasswordField('Confirm password',
                                 validators=[DataRequired(), EqualTo('password', message='Password must match')],
                                 render_kw={'placeholder': 'Retype password'})
    gender = RadioField('your gender', choices=[(True, 'male'), (False, 'female')])
    street = StringField('street', validators=[DataRequired()], render_kw={'placeholder': 'street'})
    city = StringField('City', validators=[DataRequired()], render_kw={'placeholder': 'City'})
    province = SelectField('State', validators=[DataRequired()], choices=[('assuit', 'assuit'), ('aswan', 'aswan'), (
        'monufia', 'mounifia')])  # ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax
    country = SelectField('Country', validators=[DataRequired()],
                          choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('Sa', 'Saudi')])
    submit = SubmitField('Register')


class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    address_street = StringField("address line")
    address_city = StringField('City', render_kw={'placeholder': 'city'})
    address_province = SelectField('province', choices=[('assuit', 'assuit'), ('menofia', 'menofia')])
    address_country = SelectField('country', choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('sa', 'Saudi')])
    submit = SubmitField('Update')

    # def check_email(self, field):
    #     if Users.query.filter_by(email=field.data).first():
    #         raise ValidationError('This email is already exists login instead')

# class resetForm():
#     email = StringField('your email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'your email'})
#     submit = SubmitField('Send reset Email')
