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

# Login functionality, Part 1
from os import urandom
app.config["SECRET_KEY"] = urandom(99)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


# Roles in login_required
from functools import wraps

def login_required(roles=["ANY"]):
   def wrapper(fn):
      @wraps(fn)
      def decorated_view(*args, **kwargs):
         if not current_user:
            return login_manager.unauthorized()

         if not current_user.is_authenticated:
            return login_manager.unauthorized()
            
         unauthorized = False

         if roles[0] != "ANY":
            unauthorized = True
             
            for i in roles:
               if current_user.get_userrole() == i:
                  unauthorized = False
                  break

         if unauthorized:
            return login_manager.unauthorized()
            
         return fn(*args, **kwargs)
      return decorated_view
   return wrapper


# Read views and models files (Oman sovelluksen toiminnallisuudet) 
from application import views
from application.threads import models, views
from application.auth import models, views
from application.posts import models, views


# Login functionality, Part 2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Create/Reset database tables

#db.drop_all()

try: 
    db.create_all()
except:
    pass





