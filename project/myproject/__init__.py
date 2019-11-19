from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykeyasdfghjklsdfghnjm'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codeXz:hpprobook450g3*@127.0.0.1/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# --------------- BUILD
db = SQLAlchemy(app)
Migrate(app, db)

# ---------------- LOGIN
login = LoginManager()
login.init_app(app)
login.login_view = 'users.login'

# ----------------- REGISTER_THE_BLUEPRINT
