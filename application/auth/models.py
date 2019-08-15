from application import db
from application.models import Base 

class User(Base):
   __tablename__ = "account"

   name = db.Column(db.String(255), nullable=False)
   username = db.Column(db.String(255), nullable=False)
   password = db.Column(db.String(255), nullable=False)
   admin = db.Column(db.Boolean, nullable=False)

   threads = db.relationship("Thread", backref='account', lazy=True)

   def __init__(self, name, username, password, admin):
      self.name = name
      self.username = username
      self.password = password
      self.admin = admin
  
   def get_id(self):
      return self.id

   def is_active(self):
      return True

   def is_anonymous(self):
      return False

   def is_authenticated(self):
      return True
