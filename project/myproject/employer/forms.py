from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()],
                        render_kw={'placeholder': 'Email', 'class': 'form-control'})
    username = StringField('username', validators=[InputRequired()],
                           render_kw={'placeholder': 'Username', 'class': 'form-control'})
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=6, message='your password is too short'),
                                         EqualTo('pass_confirm', message='Passwords must match')],
                             render_kw={'placeholder': 'Password', 'class': 'form-control'})
    pass_confirm = PasswordField('Confirm Password',
                                 validators=[InputRequired()],
                                 render_kw={'placeholder': 'confirm password', 'class': 'form-control'})
    phone_number = StringField('your phone number', validators=[InputRequired(), DataRequired(), Length(
        min=6, max=20, message='your password is too short')], render_kw={'placeholder': 'your phone number',
                                                                          'class': 'form-control'})
    gender = RadioField('your gender', choices=[('True', 'male'), ('False', 'female')])
    street = StringField('street', validators=[DataRequired()],
                         render_kw={'placeholder': 'street', 'class': 'form-control'})
    city = StringField('City', validators=[DataRequired()], render_kw={'placeholder': 'City', 'class': 'form-control'})

    # -------------------------------------

    province = SelectField('State', validators=[DataRequired()], choices=[('Asyut Governorate', 'Asyut Governorate'),
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

                                                                          ])

    # ------------------------- ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax

    country = SelectField('Country', validators=[DataRequired()],
                          choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('Sa', 'Saudi')])
    submit = SubmitField('Register', render_kw={'class': 'btn btn-primary'})


class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'class': 'form-control'})
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    phone_number = StringField('phone number', validators=[DataRequired()])
    address_street = StringField("address line", render_kw={'placeholder': 'Street', 'class': 'form-control'})
    address_city = StringField('City', render_kw={'placeholder': 'city', 'class': 'form-control'})
    address_province = SelectField('province', choices=[('assuit', 'assuit'), ('menofia', 'menofia')])
    address_country = SelectField('country', choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('sa', 'Saudi')])
    submit = SubmitField('Update', render_kw={'placeholder': 'btn btn-primary'})


class CreateJob(FlaskForm):
    title = StringField('Title', validators=[DataRequired()],
                        render_kw={'placeholder': 'Title', 'class': 'form-control'})
    text = TextAreaField('description for the Job', validators=[DataRequired()],
                         render_kw={'placeholder': 'write job description', 'class': 'form-control'})
    # coordinates_Latitude = StringField('latitude')
    # coordinates_Longitude = StringField('longitude')
    # media = FileField(validators=[FileAllowed(['jpg', 'png', 'gif', 'mp4', 'mkv'])])
    phone_number = StringField('contact for the job', validators=[DataRequired()],render_kw={'placeholder':'phone to be contacted on'})
    street = StringField('address line',validators=[DataRequired()],render_kw={'placeholder':'address'})
    city = StringField('City',validators=[DataRequired()],render_kw={'placeholder':'City'})
    province = SelectField('province',choices= [('Asyut Governorate', 'Asyut Governorate'),
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

                                                                      ],validators=[DataRequired()])
    country = SelectField('country', choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('sa', 'Saudi')])
    submit = SubmitField('Post')




provinces = [('Asyut Governorate', 'Asyut Governorate'),
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

                                                                      ]
