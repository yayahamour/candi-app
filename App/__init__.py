from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec1265123131qsqz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidature.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from App import routes
from App import models