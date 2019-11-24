from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Email','class':'form-control'})
    username = StringField('username', validators=[InputRequired()], render_kw={'placeholder': 'Username','class':'form-control'})
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=6, message='your password is too short')], EqualTo('pass_confirm', message='Passwords must match')],
                             render_kw={'placeholder': 'Password','class':'form-control'})
    pass_confirm = PasswordField('Confirm Password',
                                 validators=[InputRequired()], render_kw={'placeholder': 'confirm password','class':'form-control'})
    phone_number = StringField('your phone number',validators=[InputRequired(),DataRequired(), Length(min=6, max=20, message='your password is too short')]],render_kw={'placeholder':'your phone number','class':'form-control'})
    gender = RadioField('your gender', choices=[(True, 'male'), (False, 'female')])
    street = StringField('street', validators=[DataRequired()], render_kw={'placeholder': 'street','class':'form-control'})
    city = StringField('City', validators=[DataRequired()], render_kw={'placeholder': 'City','class':'form-control'})
    province = SelectField('State', validators=[DataRequired()], choices=[('assuit', 'assuit'), ('aswan', 'aswan'), (
        'monufia', 'mounifia')])  # ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax
    country = SelectField('Country', validators=[DataRequired()],
                          choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('Sa', 'Saudi')])
    submit = SubmitField('Register',render_kw={'class':'btn btn-primary'})


class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={'class':'form-control'})
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    address_street = StringField("address line",render_kw={'placeholder':'Street','class':'form-control'})
    address_city = StringField('City', render_kw={'placeholder': 'city','class':'form-control'})
    address_province = SelectField('province', choices=[('assuit', 'assuit'), ('menofia', 'menofia')])
    address_country = SelectField('country', choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('sa', 'Saudi')])
    submit = SubmitField('Update',render_kw={'placeholder':'btn btn-primary'})


class CreateJob(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={'placeholder': 'Title','class':'form-control'})
    text = TextAreaField('Text', validators=[DataRequired()],render_kw={'placeholder': 'write job description','class':'form-control'})
    coordinates_Latitude = StringField('latitude')
    coordinates_Longtitude = StringField('longtitude')
    # media = FileField(validators=[FileAllowed(['jpg', 'png', 'gif', 'mp4', 'mkv'])])
    submit = SubmitField('Post')
