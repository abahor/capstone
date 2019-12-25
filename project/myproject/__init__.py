import string
from functools import wraps
from random import choice, randint

from flask import Flask, url_for, request, abort
from flask_babel import Babel, gettext
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager, current_user
from flask_mail import Mail
# from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_admin.contrib.sqla import ModelView
# from flask_googlemaps import GoogleMaps
import flask_whooshalchemy as wa

# from myproject.models import Users, Jobs

app = Flask(__name__)

app.config['SECRET_KEY'] = 'My_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codeXz:hpprobook450g3*@127.0.0.1/capstone'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['WTF_I18N_ENABLED'] = True
# admin = Admin(app)

# app.config['GOOGLEMAPS_KEY'] = 'AIzaSyDhCWI6M6yqMrDHBLxxTqKgfzZ-iTjaV9o'


# -------- Babel
babel = Babel(app, default_locale='en')


@babel.localeselector
def get_locale():
    try:
        if str(request.url_rule).split('/')[1] == 'admin':
            return None
    except:
        return None
    # print(request.accept_languages.best_match(['ar', 'en']))
    # return 'ar'
    return request.accept_languages.best_match(['ar', 'en'])


# --------------- BUILD
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ------- dos attack protection
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10000 per day", "300 per hour"]
)

# ----- GoogleMaps
# GoogleMaps(app)

# admin.add_view(ModelView(Users,db.session))
# admin.add_view(ModelView(Jobs,db.session))

# ----- Mail ----
app.config.update(
    debug=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='khalidgamal3030@gmail.com',
    MAIL_PASSWORD='khalid123456789'
)
mail = Mail(app)

# ---------------- LOGIN
login = LoginManager()
login.init_app(app)
login.login_view = 'mained.login'
login.refresh_view = 'mained.change'
login.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)


# login.session_protection = "strong"


# --- useful functions
def detect(current, branch):
    try:
        if not current.is_authenticated:
            return url_for(f'main.{branch}')
        elif current.employer:
            return url_for(f'employer.{branch}')
        elif not current.employer:
            return url_for(f'employee.{branch}')
        else:
            return '/'
    except:
        return '/'


def random_code():
    s = "".join(choice(string.digits) for x in range(randint(1, 8)))
    return s


def check_cat(f):
    @wraps(f)
    def wra(*args, **kwargs):
        p = str(request.url_rule).split('/')
        if current_user.employer and p[1] == 'employer':
            return f(*args, **kwargs)
        elif not current_user.employer and p[1] == 'employee':
            return f(*args, **kwargs)
        else:
            return abort(404)

    return wra


@app.template_filter('province_translate')
def translate(value):
    return gettext(value)

#
@app.template_filter('country_translate')
def control(value):
    if value == 'Jo':
        return gettext('Jordan')
    elif value == 'Sa':
        return gettext('Saudi')
    else:
        return gettext('Egypt')

# ----- importing Blueprints
# noinspection PyUnresolvedReferences
from myproject.employee.views import employee
from myproject.employer.view import employer
from myproject.main.main import mained

# ----------------- REGISTER_THE_BLUEPRINT
app.register_blueprint(employee)
app.register_blueprint(employer)
app.register_blueprint(mained)

# from myproject.models import Users, Jobs
# ---- Admin
# admin = Admin(app)
