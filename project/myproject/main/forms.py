from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Email, Length


class Login(FlaskForm):
    email = StringField(lazy_gettext('Email'),
                        validators=[DataRequired(), Email()],
                        render_kw={}, _translations=True)
    password = PasswordField(lazy_gettext('Password'),
                             validators=[DataRequired(),
                                         Length(min=6, message=lazy_gettext('your password is too short try again'))],
                             render_kw={'placeholder': lazy_gettext('password')})
    submit = SubmitField(lazy_gettext('Login'))


class ResetForm(FlaskForm):
    email = StringField(lazy_gettext('your email'), validators=[DataRequired(), Email()],
                        render_kw={'placeholder': lazy_gettext('your email')})
    submit = SubmitField(lazy_gettext('Send reset Email'))


class FormRecover(FlaskForm):
    password = PasswordField(lazy_gettext('The new password'), validators=[DataRequired()],
                             render_kw={'placeholder': lazy_gettext('your new password'),
                                        'class': 'form-control'})
    submit = SubmitField(lazy_gettext('Change'))
