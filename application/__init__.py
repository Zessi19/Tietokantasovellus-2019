# Use Flask
from flask import Flask
app = Flask(__name__)

# Jinja & Moment.js (Timestamp parser)
from .momentjs import momentjs
app.jinja_env.globals['momentjs'] = momentjs

# Use SQLalchemy or Heroku DataBase
import os
from flask_sqlalchemy import SQLAlchemy

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
   app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///threads.db"
   app.config["SQLALCHEMY_ECHO"] = True

# Create db-object, which is used to handle database
db = SQLAlchemy(app)


# Read views and models files (Oman sovelluksen toiminnallisuudet) 
from application import views
from application.threads import models, views
from application.auth import models, views
from application.posts import models, views


# Login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(99)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



# Reset all datatables
#db.drop_all()

# Create all datatables
try: 
    db.create_all()
except:
    pass
