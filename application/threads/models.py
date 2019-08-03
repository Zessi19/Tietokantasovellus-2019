from application import db

class Thread(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   subject = db.Column(db.String(255), nullable=False)
   created = db.Column(db.DateTime, default=db.func.current_timestamp())

   def __init__(self, subject):
      self.subject = subject

