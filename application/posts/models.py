from application import db
from application.models import Base

from sqlalchemy.sql import text


class Post(Base):
   message = db.Column(db.Text, nullable=False)
   account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
   thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

   def __init__(self, message):
      self.message = message


   @staticmethod
   def get_posts_in_thread(threadId):
      statement = text("SELECT Account.username, Post.id, Post.message, Post.created, Post.modified FROM Post"
                  " LEFT JOIN Thread ON Thread.id = Post.thread_id"
                  " LEFT JOIN Account ON Account.id = Post.account_id"
                  " WHERE Thread.id = :threadId"
                  " ORDER BY Post.created ASC").params(threadId=threadId)
      res = db.engine.execute(statement)

      response = []
      for row in res:
         response.append([row[0], row[1], row[2], row[3], row[4]]);

      return response

