from application import db

class User(db.Model):
   __tablename__ = "account"
   id = db.Column(db.Integer, primary_key=True)

   name = db.Column(db.String(255), nullable=False)
   username = db.Column(db.String(255), nullable=False)
   password = db.Column(db.String(255), nullable=False)
   
   admin = db.Column(db.Boolean, nullable=False)   
   created = db.Column(db.DateTime, default=db.func.current_timestamp())
   modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

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
