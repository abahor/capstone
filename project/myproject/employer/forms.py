from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Email'})
    username = StringField('username', validators=[InputRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password',
                             validators=[InputRequired(), EqualTo('pass_confirm', message='Passwords must match')],
                             render_kw={'placeholder': 'Password'})
    pass_confirm = PasswordField('Confirm Password',
                                 validators=[InputRequired()], render_kw={'placeholder': 'confirm password'})
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


class CreateJob(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={'placeholder': 'Title'})
    text = TextAreaField('Text', render_kw={'placeholder': 'What do want to tell to the world?'})
    # media = FileField(validators=[FileAllowed(['jpg', 'png', 'gif', 'mp4', 'mkv'])])
    submit = SubmitField('Post')
