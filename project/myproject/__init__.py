import string
from random import choice, randint

from flask import Flask, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykeyasdfghjklsdfghnjm'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codeXz:hpprobook450g3*@127.0.0.1/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# --------------- BUILD
db = SQLAlchemy(app)
Migrate(app, db)

# ------- dos attack protection
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10000 per day", "300 per hour"]
)

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
login.login_view = 'users.login'
login_manager.refresh_view = 'main.change'
login_manager.session_protection = "strong"
# ----------------- REGISTER_THE_BLUEPRINT
from myproject.employee.views import employee
from myproject.employer.views import employer

app.register_blueprint(employee)
app.register_blueprint(employer)


# --- useful functions
def detect(current,branch):
    if current.is_authenticated != True:
        return '/'
    elif current.employer == True:
        return url_for('employer.%s'%branch)
    elif current.employer != True:
        return url_for('employee.%s'%branch)
    else:
        return '/'


def randomcode():
    s = "".join(choice(string.digits) for x in range(randint(1, 8)))
    return s
