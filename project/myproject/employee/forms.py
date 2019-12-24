from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired
from .util import Unique
# from wtforms.validators import
from myproject.models import Users


class RegistrationForm(FlaskForm):
    email = StringField(lazy_gettext('Email'), validators=[DataRequired(), Email(), Unique(
        Users,
        Users.email,
        message=lazy_gettext('There is already an account with that email.'))],
                        render_kw={'placeholder': lazy_gettext('enter your email'), 'class': 'form-control'})
    username = StringField(lazy_gettext('username'), validators=[DataRequired()],
                           render_kw={'placeholder': lazy_gettext('username')})
    password = PasswordField(lazy_gettext('Password'),
                             validators=[DataRequired(),
                                         Length(min=6, message=lazy_gettext('your password is too short'))],
                             render_kw={'placeholder': lazy_gettext('Password'), 'class': 'form-control'})
    pass_confirm = PasswordField(lazy_gettext('Confirm password'),
                                 validators=[DataRequired(),
                                             EqualTo('password', message=lazy_gettext('Password must match'))],
                                 render_kw={'placeholder': lazy_gettext('Retype password'), 'class': 'form-control'})
    phone_number = StringField(lazy_gettext('your phone number'), validators=[InputRequired(), Length(min=6, max=20,
                                                                                                      message=lazy_gettext(
                                                                                                          'your password '
                                                                                                          'is too short'))],
                               render_kw={'placeholder': lazy_gettext('your phone number'), 'class': 'form-control'})
    gender = RadioField(lazy_gettext('your gender'),
                        choices=[('True', lazy_gettext('male')), ('', lazy_gettext('female'))])
    street = StringField(lazy_gettext('street'), validators=[DataRequired()],
                         render_kw={'placeholder': lazy_gettext('street'), 'class': 'form-control'})
    city = StringField(lazy_gettext('City'), validators=[DataRequired()],
                       render_kw={'placeholder': lazy_gettext('City'), 'class': 'form-control'})
    province = SelectField(lazy_gettext('State'), validators=[DataRequired()],
                           choices=[('Asyut Governorate', 'Asyut Governorate'),
                                    ('Aswan Governorate', 'Aswan Governorate'), (
                                        "Alexandria Governorate",
                                        "Alexandria Governorate"), (
                                        'Beheira Governorate',
                                        'Beheira Governorate'),
                                    ('Beni Suef Governorate',
                                     'Beni Suef Governorate'),
                                    ('Cairo Governorate', 'Cairo Governorate'), (
                                        'Dakahlia Governorate',
                                        'Dakahlia Governorate'), (
                                        'Damietta Governorate',
                                        'Damietta Governorate'),
                                    ('Faiyum Governorate', 'Faiyum Governorate'),
                                    (
                                        'Gharbia Governorate',
                                        'Gharbia Governorate'),
                                    ('Giza Governorate', 'Giza Governorate'), (
                                        'Ismailia Governorate',
                                        'Ismailia Governorate'), (
                                        'Kafr el-Sheikh Governorate',
                                        'Kafr el-Sheikh Governorate'),
                                    ('Luxor Governorate', 'Luxor Governorate'), (
                                        'Matrouh Governorate',
                                        'Matrouh Governorate'),
                                    ('Minya Governorate', 'Minya Governorate'), (
                                        'Monufia Governorate',
                                        'Monufia Governorate'),
                                    ('New Valley Governorate',
                                     'New Valley Governorate'), (
                                        'North Sinai Governorate',
                                        'North Sinai Governorate'), (
                                        'Port Said Governorate',
                                        'Port Said Governorate'), (
                                        'Qalyubia Governorate',
                                        'Qalyubia Governorate'),
                                    ('Qena Governorate', 'Qena Governorate'), (
                                        'Red Sea Governorate',
                                        'Red Sea Governorate'),
                                    ('Sohag Governorate', 'Sohag Governorate'), (
                                        'South Sinai Governorate',
                                        'South Sinai Governorate'),
                                    ('Suez Governorate', 'Suez Governorate'), (
                                        'Al Hudud ash Shamaliyah',
                                        'Al Hudud ash Shamaliyah'),
                                    ('Al Bahah', 'Al Bahah'),
                                    ('Al Jawf', 'Al Jawf'),
                                    ('Al Madinah', 'Al Madinah'),
                                    ('Al Qasim', 'Al Qasim'),
                                    ('Ar Riyad', 'Ar Riyad'),
                                    ('Ash Sharqiyah', 'Ash Sharqiyah'),
                                    ('Asir', 'Asir'), ('Hail', 'Hail'),
                                    ('Jizan', 'Jizan'), ('Makkah', 'Makkah'),
                                    ('Najran', 'Najran'), ('Tabuk', 'Tabuk'),
                                    ('Ajlun', 'Ajlun'),
                                    ('Al Aqabah', 'Al Aqabah'),
                                    ('Al Balqa', 'Al Balqa'),
                                    ('Al Karak', 'Al Karak'),
                                    ('Al Mafraq', 'Al Mafraq'),
                                    ('Amman', 'Amman'),
                                    ('At Tafilah', 'At Tafilah'),
                                    ('Az Zarqa', 'Az Zarqa'), ('Irbid', 'Irbid'),
                                    ('Jarash', 'Jarash'), ('Madaba', 'Madaba'),
                                    ('Maan', 'Maan')

                                    ])  # ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax
    country = SelectField(lazy_gettext('Country'), validators=[DataRequired()],
                          choices=[('Eg', lazy_gettext('Egypt')), ('Jo', lazy_gettext('Jordan')),
                                   ('Sa', lazy_gettext('Saudi'))])
    submit = SubmitField(lazy_gettext('Register'))


class UpdateForm(FlaskForm):
    username = StringField(lazy_gettext('Username'), validators=[DataRequired()], render_kw={'class': 'form-control'})
    picture = FileField(lazy_gettext('Update Profile Picture'), validators=[FileAllowed(['jpg', 'png', 'gif'])])
    phone_number = StringField(lazy_gettext('phone number'), validators=[DataRequired()],
                               render_kw={'placeholder': lazy_gettext('phone number')})
    street = StringField(lazy_gettext("address line"),
                         render_kw={'placeholder': lazy_gettext('Street'), 'class': 'form-control'})
    city = StringField(lazy_gettext('City'), validators=[DataRequired()],
                       render_kw={'placeholder': lazy_gettext('city'), 'class': 'form-control'})
    province = SelectField(lazy_gettext('province'), validators=[DataRequired()],
                           choices=[('Asyut Governorate', 'Asyut Governorate'),
                                    ('Aswan Governorate', 'Aswan Governorate'), (
                                        "Alexandria Governorate",
                                        "Alexandria Governorate"), (
                                        'Beheira Governorate',
                                        'Beheira Governorate'),
                                    ('Beni Suef Governorate',
                                     'Beni Suef Governorate'),
                                    ('Cairo Governorate', 'Cairo Governorate'), (
                                        'Dakahlia Governorate',
                                        'Dakahlia Governorate'), (
                                        'Damietta Governorate',
                                        'Damietta Governorate'),
                                    ('Faiyum Governorate', 'Faiyum Governorate'),
                                    (
                                        'Gharbia Governorate',
                                        'Gharbia Governorate'),
                                    ('Giza Governorate', 'Giza Governorate'), (
                                        'Ismailia Governorate',
                                        'Ismailia Governorate'), (
                                        'Kafr el-Sheikh Governorate',
                                        'Kafr el-Sheikh Governorate'),
                                    ('Luxor Governorate', 'Luxor Governorate'), (
                                        'Matrouh Governorate',
                                        'Matrouh Governorate'),
                                    ('Minya Governorate', 'Minya Governorate'), (
                                        'Monufia Governorate',
                                        'Monufia Governorate'),
                                    ('New Valley Governorate',
                                     'New Valley Governorate'), (
                                        'North Sinai Governorate',
                                        'North Sinai Governorate'), (
                                        'Port Said Governorate',
                                        'Port Said Governorate'), (
                                        'Qalyubia Governorate',
                                        'Qalyubia Governorate'),
                                    ('Qena Governorate', 'Qena Governorate'), (
                                        'Red Sea Governorate',
                                        'Red Sea Governorate'),
                                    ('Sohag Governorate', 'Sohag Governorate'), (
                                        'South Sinai Governorate',
                                        'South Sinai Governorate'),
                                    ('Suez Governorate', 'Suez Governorate'), (
                                        'Al Hudud ash Shamaliyah',
                                        'Al Hudud ash Shamaliyah'),
                                    ('Al Bahah', 'Al Bahah'),
                                    ('Al Jawf', 'Al Jawf'),
                                    ('Al Madinah', 'Al Madinah'),
                                    ('Al Qasim', 'Al Qasim'),
                                    ('Ar Riyad', 'Ar Riyad'),
                                    ('Ash Sharqiyah', 'Ash Sharqiyah'),
                                    ('Asir', 'Asir'), ('Hail', 'Hail'),
                                    ('Jizan', 'Jizan'), ('Makkah', 'Makkah'),
                                    ('Najran', 'Najran'), ('Tabuk', 'Tabuk'),
                                    ('Ajlun', 'Ajlun'),
                                    ('Al Aqabah', 'Al Aqabah'),
                                    ('Al Balqa', 'Al Balqa'),
                                    ('Al Karak', 'Al Karak'),
                                    ('Al Mafraq', 'Al Mafraq'),
                                    ('Amman', 'Amman'),
                                    ('At Tafilah', 'At Tafilah'),
                                    ('Az Zarqa', 'Az Zarqa'), ('Irbid', 'Irbid'),
                                    ('Jarash', 'Jarash'), ('Madaba', 'Madaba'),
                                    ('Maan', 'Maan')

                                    ], _translations=True)
    country = SelectField(lazy_gettext('country'), validators=[DataRequired()],
                          choices=[('Eg', lazy_gettext('Egypt')), ('Jo', lazy_gettext('Jordan')),
                                   ('Sa', lazy_gettext('Saudi'))], _translations=True)
    submit = SubmitField(lazy_gettext('Update'), render_kw={'class': 'btn btn-primary'})

    # def check_email(self, field):
    #     if Users.query.filter_by(email=field.data).first():
    #         raise ValidationError('This email is already exists login instead')

# class resetForm():
#     email = StringField('your email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'your email'})
#     submit = SubmitField('Send reset Email')
