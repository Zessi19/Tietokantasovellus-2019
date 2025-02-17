from application import db
from application.models import Base

from sqlalchemy.sql import text


class Post(Base):
   message = db.Column(db.Text, nullable=False)
   priority = db.Column(db.Integer, nullable=False)

   account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
   thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

   def __init__(self, message, priority):
      self.message = message
      self.priority = priority


   # List of User and Post data from all posts in single Thread(threadId)
   @staticmethod
   def get_posts_in_thread(threadId):
      statement = text("SELECT Account.id, Account.username, Post.id, Post.message, Post.created, Post.modified FROM Post"
                  " LEFT JOIN Thread ON Thread.id = Post.thread_id"
                  " LEFT JOIN Account ON Account.id = Post.account_id"
                  " WHERE Thread.id = :threadId"
                  " ORDER BY Post.priority DESC, Post.created ASC").params(threadId=threadId)
      res = db.engine.execute(statement)

      response = []
      for row in res:
         response.append([row[0], row[1], row[2], row[3], row[4], row[5]]);

      return response

   # Total number of posts in database
   @staticmethod
   def total_posts():
      statement = text("SELECT COUNT(*) FROM Post")
      res = db.engine.execute(statement)

      for row in res:
         response = row[0]
      return response
