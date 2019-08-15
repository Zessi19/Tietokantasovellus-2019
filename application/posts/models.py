from application import db
from application.models import Base

from sqlalchemy.sql import text


class Post(Base):
   message = db.Column(db.Text, nullable=False)
   account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
   thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

   def __init__(self, content):
      self.content = content
