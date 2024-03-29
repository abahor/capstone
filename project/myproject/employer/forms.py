from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length

from myproject.models import Users
from .util import Unique


class RegistrationForm(FlaskForm):
    email = StringField(lazy_gettext('Email'), validators=[InputRequired(), Email(), Unique(
        Users,
        Users.email,
        lazy_gettext('There is already an account with that email.'))],
                        render_kw={'placeholder': lazy_gettext('Email'), 'class': 'form-control'})
    username = StringField(lazy_gettext('username'), validators=[InputRequired()],
                           render_kw={'placeholder': lazy_gettext('Username'), 'class': 'form-control'})
    password = PasswordField(lazy_gettext('Password'),
                             validators=[InputRequired(),
                                         Length(min=6, message=lazy_gettext('your password is too short')),
                                         EqualTo('pass_confirm', message=lazy_gettext('Passwords must match'))],
                             render_kw={'placeholder': lazy_gettext('Password'), 'class': 'form-control'})
    pass_confirm = PasswordField(lazy_gettext('Confirm Password'),
                                 validators=[InputRequired()],
                                 render_kw={'placeholder': lazy_gettext('Confirm password'), 'class': 'form-control'})
    phone_number = StringField(lazy_gettext('your phone number'), validators=[InputRequired(), DataRequired(), Length(
        min=6, max=20, message=lazy_gettext('your password is too short'))], render_kw={
        'placeholder': lazy_gettext('your phone number'), 'class': 'form-control'})
    gender = RadioField(lazy_gettext('your gender'),
                        choices=[('True', lazy_gettext('male')), ('False', lazy_gettext('female'))])
    street = StringField(lazy_gettext('street'), validators=[DataRequired()],
                         render_kw={'placeholder': lazy_gettext('street'), 'class': 'form-control'})
    city = StringField(lazy_gettext('City'), validators=[DataRequired()], render_kw={
        'placeholder': lazy_gettext('city'), 'class': 'form-control'})

    # -------------------------------------

    province = SelectField(lazy_gettext('State'), validators=[DataRequired()],
                           choices=[('Asyut Governorate', lazy_gettext('Asyut Governorate')),
                                    ('Aswan Governorate', lazy_gettext('Aswan Governorate')),
                                    ("Alexandria Governorate", lazy_gettext("Alexandria Governorate")),
                                    ('Beheira Governorate', lazy_gettext('Beheira Governorate')),
                                    ('Beni Suef Governorate',
                                     lazy_gettext('Beni Suef Governorate')),
                                    ('Cairo Governorate', lazy_gettext('Cairo Governorate')),
                                    ('Dakahlia Governorate', lazy_gettext('Dakahlia Governorate')),
                                    ('Damietta Governorate', lazy_gettext('Damietta Governorate')),
                                    ('Faiyum Governorate', lazy_gettext('Faiyum Governorate')),
                                    ('Gharbia Governorate', lazy_gettext('Gharbia Governorate')),
                                    ('Giza Governorate', lazy_gettext('Giza Governorate')),
                                    ('Ismailia Governorate', lazy_gettext('Ismailia Governorate')),
                                    (
                                        'Kafr el-Sheikh Governorate',
                                        lazy_gettext('Kafr el-Sheikh Governorate')),
                                    ('Luxor Governorate', lazy_gettext('Luxor Governorate')), (
                                        'Matrouh Governorate',
                                        lazy_gettext('Matrouh Governorate')),
                                    ('Minya Governorate', lazy_gettext('Minya Governorate')), (
                                        'Monufia Governorate',
                                        lazy_gettext('Monufia Governorate')),
                                    ('New Valley Governorate',
                                     lazy_gettext('New Valley Governorate')), (
                                        'North Sinai Governorate',
                                        lazy_gettext('North Sinai Governorate')),
                                    ('Port Said Governorate', lazy_gettext('Port Said Governorate')),
                                    ('Qalyubia Governorate',
                                     lazy_gettext('Qalyubia Governorate')),
                                    ('Qena Governorate', lazy_gettext('Qena Governorate')), (
                                        'Red Sea Governorate',
                                        lazy_gettext('Red Sea Governorate')),
                                    ('Sohag Governorate', lazy_gettext('Sohag Governorate')), (
                                        'South Sinai Governorate',
                                        lazy_gettext('South Sinai Governorate')),
                                    ('Suez Governorate', lazy_gettext('Suez Governorate')), (
                                        'Al Hudud ash Shamaliyah',
                                        lazy_gettext('Al Hudud ash Shamaliyah')),
                                    ('Al Bahah', lazy_gettext('Al Bahah')),
                                    ('Al Jawf', lazy_gettext('Al Jawf')),
                                    ('Al Madinah', lazy_gettext('Al Madinah')),
                                    ('Al Qasim', lazy_gettext('Al Qasim')),
                                    ('Ar Riyad', lazy_gettext('Ar Riyad')),
                                    ('Ash Sharqiyah', lazy_gettext('Ash Sharqiyah')),
                                    ('Asir', lazy_gettext('Asir')), ('Hail', lazy_gettext('Hail')),
                                    ('Jizan', lazy_gettext('Jizan')), ('Makkah', lazy_gettext('Makkah')),
                                    ('Najran', lazy_gettext('Najran')), ('Tabuk', lazy_gettext('Tabuk')),
                                    ('Ajlun', lazy_gettext('Ajlun')),
                                    ('Al Aqabah', lazy_gettext('Al Aqabah')),
                                    ('Al Balqa', lazy_gettext('Al Balqa')),
                                    ('Al Karak', lazy_gettext('Al Karak')),
                                    ('Al Mafraq', lazy_gettext('Al Mafraq')),
                                    ('Amman', lazy_gettext('Amman')),
                                    ('At Tafilah', lazy_gettext('At Tafilah')),
                                    ('Az Zarqa', lazy_gettext('Az Zarqa')), ('Irbid', lazy_gettext('Irbid')),
                                    ('Jarash', lazy_gettext('Jarash')), ('Madaba', lazy_gettext('Madaba')),
                                    ('Maan', lazy_gettext('Maan'))

                                    ])

    # ------------------------- ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax

    country = SelectField(lazy_gettext('Country'), validators=[DataRequired()],
                          choices=[('Eg', lazy_gettext('Egypt')), ('Jo', lazy_gettext('Jordan')),
                                   ('Sa', lazy_gettext('Saudi'))])
    submit = SubmitField(lazy_gettext('Register'), render_kw={'class': 'btn btn-primary'})


class UpdateForm(FlaskForm):
    username = StringField(lazy_gettext('Username'), validators=[DataRequired()],
                           render_kw={'class': 'form-control', 'placeholder': lazy_gettext('username')})
    picture = FileField(lazy_gettext('Update Profile Picture'), validators=[FileAllowed(['jpg', 'png', 'gif'])])
    phone_number = StringField(lazy_gettext('phone number'), validators=[DataRequired()],
                               render_kw={'placeholder': lazy_gettext('phone number')})
    street = StringField(lazy_gettext("address line"),
                         render_kw={'placeholder': lazy_gettext('Street'), 'class': 'form-control'})
    city = StringField(lazy_gettext('City'), validators=[DataRequired()],
                       render_kw={'placeholder': lazy_gettext('city'), 'class': 'form-control'})
    province = SelectField(lazy_gettext('province'), validators=[DataRequired()],
                           choices=[('Asyut Governorate', lazy_gettext('Asyut Governorate')),
                                    ('Aswan Governorate', lazy_gettext('Aswan Governorate')),
                                    ("Alexandria Governorate", lazy_gettext("Alexandria Governorate")),
                                    ('Beheira Governorate', lazy_gettext('Beheira Governorate')),
                                    ('Beni Suef Governorate', lazy_gettext('Beni Suef Governorate')),
                                    ('Cairo Governorate', lazy_gettext('Cairo Governorate')),
                                    ('Dakahlia Governorate', lazy_gettext('Dakahlia Governorate')),
                                    ('Damietta Governorate', lazy_gettext('Damietta Governorate')),
                                    ('Faiyum Governorate', lazy_gettext('Faiyum Governorate')),
                                    ('Gharbia Governorate', lazy_gettext('Gharbia Governorate')),
                                    ('Giza Governorate', lazy_gettext('Giza Governorate')),
                                    ('Ismailia Governorate', lazy_gettext('Ismailia Governorate')),
                                    (
                                        'Kafr el-Sheikh Governorate',
                                        lazy_gettext('Kafr el-Sheikh Governorate')),
                                    ('Luxor Governorate', lazy_gettext('Luxor Governorate')), (
                                        'Matrouh Governorate',
                                        lazy_gettext('Matrouh Governorate')),
                                    ('Minya Governorate', lazy_gettext('Minya Governorate')), (
                                        'Monufia Governorate',
                                        lazy_gettext('Monufia Governorate')),
                                    ('New Valley Governorate',
                                     lazy_gettext('New Valley Governorate')), (
                                        'North Sinai Governorate',
                                        lazy_gettext('North Sinai Governorate')),
                                    ('Port Said Governorate', lazy_gettext('Port Said Governorate')),
                                    ('Qalyubia Governorate',
                                     lazy_gettext('Qalyubia Governorate')),
                                    ('Qena Governorate', lazy_gettext('Qena Governorate')), (
                                        'Red Sea Governorate',
                                        lazy_gettext('Red Sea Governorate')),
                                    ('Sohag Governorate', lazy_gettext('Sohag Governorate')), (
                                        'South Sinai Governorate',
                                        lazy_gettext('South Sinai Governorate')),
                                    ('Suez Governorate', lazy_gettext('Suez Governorate')), (
                                        'Al Hudud ash Shamaliyah',
                                        lazy_gettext('Al Hudud ash Shamaliyah')),
                                    ('Al Bahah', lazy_gettext('Al Bahah')),
                                    ('Al Jawf', lazy_gettext('Al Jawf')),
                                    ('Al Madinah', lazy_gettext('Al Madinah')),
                                    ('Al Qasim', lazy_gettext('Al Qasim')),
                                    ('Ar Riyad', lazy_gettext('Ar Riyad')),
                                    ('Ash Sharqiyah', lazy_gettext('Ash Sharqiyah')),
                                    ('Asir', lazy_gettext('Asir')), ('Hail', lazy_gettext('Hail')),
                                    ('Jizan', lazy_gettext('Jizan')), ('Makkah', lazy_gettext('Makkah')),
                                    ('Najran', lazy_gettext('Najran')), ('Tabuk', lazy_gettext('Tabuk')),
                                    ('Ajlun', lazy_gettext('Ajlun')),
                                    ('Al Aqabah', lazy_gettext('Al Aqabah')),
                                    ('Al Balqa', lazy_gettext('Al Balqa')),
                                    ('Al Karak', lazy_gettext('Al Karak')),
                                    ('Al Mafraq', lazy_gettext('Al Mafraq')),
                                    ('Amman', lazy_gettext('Amman')),
                                    ('At Tafilah', lazy_gettext('At Tafilah')),
                                    ('Az Zarqa', lazy_gettext('Az Zarqa')), ('Irbid', lazy_gettext('Irbid')),
                                    ('Jarash', lazy_gettext('Jarash')), ('Madaba', lazy_gettext('Madaba')),
                                    ('Maan', lazy_gettext('Maan'))

                                    ])
    country = SelectField(lazy_gettext('country'), validators=[DataRequired()],
                          choices=[('Eg', lazy_gettext('Egypt')), ('Jo', lazy_gettext('Jordan')),
                                   ('Sa', lazy_gettext('Saudi'))])
    submit = SubmitField('Update', render_kw={'class': 'btn btn-primary'})


class CreateJob(FlaskForm):
    title = StringField(lazy_gettext('Title'), validators=[DataRequired()],
                        render_kw={'placeholder': lazy_gettext('Title'), 'class': 'form-control'})
    text = TextAreaField(lazy_gettext('description for the Job'), validators=[DataRequired()],
                         render_kw={'placeholder': lazy_gettext('write job description'), 'class': 'form-control'})
    # coordinates_Latitude = StringField('latitude')
    # coordinates_Longitude = StringField('longitude')
    # media = FileField(validators=[FileAllowed(['jpg', 'png', 'gif', 'mp4', 'mkv'])])

    phone_for_contact = StringField(lazy_gettext('Phone for contact'), validators=[DataRequired()],
                                    render_kw={'placeholder': lazy_gettext('Phone to be contacted on')})
    street = StringField(lazy_gettext('address line'), validators=[DataRequired()],
                         render_kw={'placeholder': lazy_gettext('address')})
    city = StringField(lazy_gettext('City'), validators=[DataRequired()],
                       render_kw={'placeholder': lazy_gettext('City')})
    province = SelectField(lazy_gettext('province'), choices=[('Asyut Governorate', lazy_gettext('Asyut Governorate')),
                                                              ('Aswan Governorate', lazy_gettext('Aswan Governorate')),
                                                              ("Alexandria Governorate",
                                                               lazy_gettext("Alexandria Governorate")),
                                                              ('Beheira Governorate',
                                                               lazy_gettext('Beheira Governorate')),
                                                              ('Beni Suef Governorate',
                                                               lazy_gettext('Beni Suef Governorate')),
                                                              ('Cairo Governorate', lazy_gettext('Cairo Governorate')),
                                                              ('Dakahlia Governorate',
                                                               lazy_gettext('Dakahlia Governorate')),
                                                              ('Damietta Governorate',
                                                               lazy_gettext('Damietta Governorate')),
                                                              (
                                                              'Faiyum Governorate', lazy_gettext('Faiyum Governorate')),
                                                              ('Gharbia Governorate',
                                                               lazy_gettext('Gharbia Governorate')),
                                                              ('Giza Governorate', lazy_gettext('Giza Governorate')),
                                                              ('Ismailia Governorate',
                                                               lazy_gettext('Ismailia Governorate')),
                                                              (
                                                                  'Kafr el-Sheikh Governorate',
                                                                  lazy_gettext('Kafr el-Sheikh Governorate')),
                                                              ('Luxor Governorate', lazy_gettext('Luxor Governorate')),
                                                              (
                                                                  'Matrouh Governorate',
                                                                  lazy_gettext('Matrouh Governorate')),
                                                              ('Minya Governorate', lazy_gettext('Minya Governorate')),
                                                              (
                                                                  'Monufia Governorate',
                                                                  lazy_gettext('Monufia Governorate')),
                                                              ('New Valley Governorate',
                                                               lazy_gettext('New Valley Governorate')), (
                                                                  'North Sinai Governorate',
                                                                  lazy_gettext('North Sinai Governorate')),
                                                              ('Port Said Governorate',
                                                               lazy_gettext('Port Said Governorate')),
                                                              ('Qalyubia Governorate',
                                                               lazy_gettext('Qalyubia Governorate')),
                                                              ('Qena Governorate', lazy_gettext('Qena Governorate')), (
                                                                  'Red Sea Governorate',
                                                                  lazy_gettext('Red Sea Governorate')),
                                                              ('Sohag Governorate', lazy_gettext('Sohag Governorate')),
                                                              (
                                                                  'South Sinai Governorate',
                                                                  lazy_gettext('South Sinai Governorate')),
                                                              ('Suez Governorate', lazy_gettext('Suez Governorate')), (
                                                                  'Al Hudud ash Shamaliyah',
                                                                  lazy_gettext('Al Hudud ash Shamaliyah')),
                                                              ('Al Bahah', lazy_gettext('Al Bahah')),
                                                              ('Al Jawf', lazy_gettext('Al Jawf')),
                                                              ('Al Madinah', lazy_gettext('Al Madinah')),
                                                              ('Al Qasim', lazy_gettext('Al Qasim')),
                                                              ('Ar Riyad', lazy_gettext('Ar Riyad')),
                                                              ('Ash Sharqiyah', lazy_gettext('Ash Sharqiyah')),
                                                              ('Asir', lazy_gettext('Asir')),
                                                              ('Hail', lazy_gettext('Hail')),
                                                              ('Jizan', lazy_gettext('Jizan')),
                                                              ('Makkah', lazy_gettext('Makkah')),
                                                              ('Najran', lazy_gettext('Najran')),
                                                              ('Tabuk', lazy_gettext('Tabuk')),
                                                              ('Ajlun', lazy_gettext('Ajlun')),
                                                              ('Al Aqabah', lazy_gettext('Al Aqabah')),
                                                              ('Al Balqa', lazy_gettext('Al Balqa')),
                                                              ('Al Karak', lazy_gettext('Al Karak')),
                                                              ('Al Mafraq', lazy_gettext('Al Mafraq')),
                                                              ('Amman', lazy_gettext('Amman')),
                                                              ('At Tafilah', lazy_gettext('At Tafilah')),
                                                              ('Az Zarqa', lazy_gettext('Az Zarqa')),
                                                              ('Irbid', lazy_gettext('Irbid')),
                                                              ('Jarash', lazy_gettext('Jarash')),
                                                              ('Madaba', lazy_gettext('Madaba')),
                                                              ('Maan', lazy_gettext('Maan'))

                                                              ], validators=[DataRequired()])

    country = SelectField(lazy_gettext('country'),
                          choices=[('Eg', lazy_gettext('Egypt')), ('Jo', lazy_gettext('Jordan')),
                                   ('Sa', lazy_gettext('Saudi'))])
    submit = SubmitField(lazy_gettext('Post'))

# provinces = [('Asyut Governorate', 'Asyut Governorate'),
#              ('Aswan Governorate', 'Aswan Governorate'), (
#                  "Alexandria Governorate",
#                  "Alexandria Governorate"), (
#                  'Beheira Governorate',
#                  'Beheira Governorate'),
#              ('Beni Suef Governorate',
#               'Beni Suef Governorate'),
#              ('Cairo Governorate', 'Cairo Governorate'), (
#                  'Dakahlia Governorate',
#                  'Dakahlia Governorate'), (
#                  'Damietta Governorate',
#                  'Damietta Governorate'),
#              ('Faiyum Governorate', 'Faiyum Governorate'),
#              (
#                  'Gharbia Governorate',
#                  'Gharbia Governorate'),
#              ('Giza Governorate', 'Giza Governorate'), (
#                  'Ismailia Governorate',
#                  'Ismailia Governorate'), (
#                  'Kafr el-Sheikh Governorate',
#                  'Kafr el-Sheikh Governorate'),
#              ('Luxor Governorate', 'Luxor Governorate'), (
#                  'Matrouh Governorate',
#                  'Matrouh Governorate'),
#              ('Minya Governorate', 'Minya Governorate'), (
#                  'Monufia Governorate',
#                  'Monufia Governorate'),
#              ('New Valley Governorate',
#               'New Valley Governorate'), (
#                  'North Sinai Governorate',
#                  'North Sinai Governorate'), (
#                  'Port Said Governorate',
#                  'Port Said Governorate'), (
#                  'Qalyubia Governorate',
#                  'Qalyubia Governorate'),
#              ('Qena Governorate', 'Qena Governorate'), (
#                  'Red Sea Governorate',
#                  'Red Sea Governorate'),
#              ('Sohag Governorate', 'Sohag Governorate'), (
#                  'South Sinai Governorate',
#                  'South Sinai Governorate'),
#              ('Suez Governorate', 'Suez Governorate'), (
#                  'Al Hudud ash Shamaliyah',
#                  'Al Hudud ash Shamaliyah'),
#              ('Al Bahah', 'Al Bahah'),
#              ('Al Jawf', 'Al Jawf'),
#              ('Al Madinah', 'Al Madinah'),
#              ('Al Qasim', 'Al Qasim'),
#              ('Ar Riyad', 'Ar Riyad'),
#              ('Ash Sharqiyah', 'Ash Sharqiyah'),
#              ('Asir', 'Asir'), ('Hail', 'Hail'),
#              ('Jizan', 'Jizan'), ('Makkah', 'Makkah'),
#              ('Najran', 'Najran'), ('Tabuk', 'Tabuk'),
#              ('Ajlun', 'Ajlun'),
#              ('Al Aqabah', 'Al Aqabah'),
#              ('Al Balqa', 'Al Balqa'),
#              ('Al Karak', 'Al Karak'),
#              ('Al Mafraq', 'Al Mafraq'),
#              ('Amman', 'Amman'),
#              ('At Tafilah', 'At Tafilah'),
#              ('Az Zarqa', 'Az Zarqa'), ('Irbid', 'Irbid'),
#              ('Jarash', 'Jarash'), ('Madaba', 'Madaba'),
#              ('Maan', 'Maan')
#
#              ]
