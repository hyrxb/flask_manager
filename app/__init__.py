from utils.config import Config
from autils import Logger
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from autils import String

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

config = Config("config.ini", "DEV")
logger = Logger(config.read("log")).logger

app = Flask(__name__)
login_manager.init_app(app)
app.config['SECRET_KEY'] = String.generate()
app.config["SQLALCHEMY_DATABASE_URI"] = config.read("DB_URL").format(
    user=config.read("DB_USER"),
    password=config.read("DB_PWD"),
    url=config.read("DB_HOST"),
    port=int(config.read("DB_PORT")),
    db=config.read("DB_NAME")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from .auth import auth
from .main import main

app.register_blueprint(auth)
app.register_blueprint(main)
