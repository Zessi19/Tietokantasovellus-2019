# use Flask
from flask import Flask
app = Flask(__name__)

# use SQLalchemy
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///threads.db"
app.config["SQLALCHEMY_ECHO"] = True

# Create db-object, which is used to handle database
db = SQLAlchemy(app)

# Read application/views.py 
from application import views

from application.threads import models
from application.threads import views

# Create all datatables
db.create_all()

# Reset all datatables
#db.drop_all()
