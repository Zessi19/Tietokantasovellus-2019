from application import db

class Thread(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   topic = db.Column(db.String(100), nullable=False)
   created = db.Column(db.DateTime, default=db.func.current_timestamp())
   modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

   def __init__(self, topic):
      self.topic = topic

