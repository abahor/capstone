from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'enter your email', 'class': 'form-control'})
    username = StringField('username', validators=[DataRequired()], render_kw={'placeholder': 'username'})
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, message='your password is too short')],
                             render_kw={'placeholder': 'Password', 'class': 'form-control'})
    pass_confirm = PasswordField('Confirm password',
                                 validators=[DataRequired(), EqualTo('password', message='Password must match')],
                                 render_kw={'placeholder': 'Retype password', 'class': 'form-control'})
    phone_number = StringField('your phone number', validators=[InputRequired(), Length(min=6, max=20,
                                                                                        message='your password is too short')],
                               render_kw={'placeholder': 'your phone number', 'class': 'form-control'})
    gender = RadioField('your gender', choices=[('True', 'male'), ('', 'female')])
    street = StringField('street', validators=[DataRequired()],
                         render_kw={'placeholder': 'street', 'class': 'form-control'})
    city = StringField('City', validators=[DataRequired()], render_kw={'placeholder': 'City', 'class': 'form-control'})
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

                                                                          ])  # ---  ---  kamel hena ya afgany # --- will be verified by the country js ajax
    country = SelectField('Country', validators=[DataRequired()],
                          choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('Sa', 'Saudi')])
    submit = SubmitField('Register')


class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'class': 'form-control'})
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])
    phone_number = StringField('phone number', validators=[DataRequired()], render_kw={'placeholder': 'phone number'})
    street = StringField("address line", render_kw={'placeholder': 'Street', 'class': 'form-control'})
    city = StringField('City', validators=[DataRequired()], render_kw={'placeholder': 'city', 'class': 'form-control'})
    province = SelectField('province', validators=[DataRequired()],
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

                                    ])
    country = SelectField('country', validators=[DataRequired()],
                          choices=[('Eg', 'Egypt'), ('Jo', 'Jordan'), ('Sa', 'Saudi')])
    submit = SubmitField('Update', render_kw={'class': 'btn btn-primary'})

    # def check_email(self, field):
    #     if Users.query.filter_by(email=field.data).first():
    #         raise ValidationError('This email is already exists login instead')

# class resetForm():
#     email = StringField('your email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'your email'})
#     submit = SubmitField('Send reset Email')
