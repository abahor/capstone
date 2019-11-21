from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from myproject.models import Users
from wtforms import SubmitField, StringField, PasswordField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegisterationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Email'})
    username = StringField('username', validators=[InputRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password',
                             validators=[InputRequired(), EqualTo('pass_confirm', message='Passwords must match')],
                             render_kw={'placeholder': 'Password'})
    pass_confirm = PasswordField('Confirm Password',
                                 validators=[InputRequired()], render_kw={'placeholder': 'confirm password'})
    gender = RadioField('your gender',choices[(True,'male'),( False,'female')])
    street = StringField('street', validators=[DataRequired()], render_kw={'placeholder': 'street'})
    city = StringField('City', validators=[DataRequired()], render_kw={'placeholder': 'City'})
    province = SelectField('State', validators=[DataRequired()], choices=[('assuit', 'assuit'), ('aswan', 'aswan'), (
        'monufia', 'mounifia')])  # ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax
    country = SelectField('Country', validators=[DataRequired()],
                          choices=[('Eg', 'Egypt'), ('Jo', 'Jorden'), ('Sa', 'Saudi')])
    submit = SubmitField('Register')

    def check_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already exists login instead')


class updateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    address_street = StringField("address line")
    address_city = StringField('City', render_kw={'placeholder': 'city'})
    address_province = SelectField('province', choices=[('assuit', 'assuit'), ('menofia', 'menofia')])
    address_country = SelectField('country', choices=[('Eg', 'Egypt'), ('Jo', 'Jorden'), ('sa', 'Saudi')])
    submit = SubmitField('Update')

    # def check_email(self, field):
    #     if Users.query.filter_by(email=field.data).first():
    #         raise ValidationError('This email is already exists login instead')


class formRecover(FlaskForm):
    password = PasswordField('The new password', validators=[DataRequired()], render_kw={'placeholder': 'your new '
                                                                                                        'password'})
    submit = SubmitField('Change')


class verifyForm(FlaskForm):
    password = PasswordField('The your current password', validators=[DataRequired()],
                             render_kw={'placeholder': 'current password'})
    submit = SubmitField('Verify')


class createJob(FlaskForm):
    title = StringField('Title', validators=[validators.DataRequired()], render_kw={'placeholder': 'Title'})
    text = TextAreaField('Text', render_kw={'placeholder': 'What do want to tell to the world?'})
    # media = FileField(validators=[FileAllowed(['jpg', 'png', 'gif', 'mp4', 'mkv'])])
    submit = SubmitField('Post')


class resetForm():
    email = StringField('your email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'your email'})
    submit = SubmitField('Send reset Email')
