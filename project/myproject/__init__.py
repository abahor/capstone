import string
from functools import wraps
from random import choice, randint

from flask import Flask, url_for, request, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager, current_user
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_googlemaps import GoogleMaps
import flask_whooshalchemy as wa

app = Flask(__name__)

app.config['SECRET_KEY'] = 'My_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codeXz:hpprobook450g3*@127.0.0.1/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['GOOGLEMAPS_KEY'] = 'AIzaSyDhCWI6M6yqMrDHBLxxTqKgfzZ-iTjaV9o'
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

# ----- Mail ----
app.config.update(
    debug=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='jousefgamal46@gmail.com',
    MAIL_PASSWORD='jousefgamal123456789'
)
mail = Mail(app)

# ---------------- LOGIN
login = LoginManager()
login.init_app(app)
login.login_view = 'mained.login'
login.refresh_view = 'mained.change'
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
        if current_user.employer == True and p[1] == 'employer':
            return f(*args, **kwargs)
        elif not current_user.employer and p[1] == 'employee':
            return f(*args, **kwargs)
        else:
            return abort(404)
    return wra



# ----- importing Blueprints
# from myproject.employee.views import employee
# from myproject.employer.view import employer
# from myproject.main.main import mained
#
# # ----------------- REGISTER_THE_BLUEPRINT
# app.register_blueprint(employee)
# app.register_blueprint(employer)
# app.register_blueprint(mained)
