from application import db
from application.models import Base

from sqlalchemy.sql import text


class User(Base):
   __tablename__ = "account"

   name = db.Column(db.String(255), nullable=False)
   username = db.Column(db.String(255), nullable=False)
   password = db.Column(db.String(255), nullable=False)
   admin = db.Column(db.Boolean, nullable=False)

   posts = db.relationship("Post", backref='account', lazy=True)

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


   @staticmethod
   def count_user_threads_and_posts(userId):
      statement = text("SELECT Post.priority, COUNT(Post.id) FROM Account"
                  " LEFT JOIN Post ON Account.id = Post.account_id"
                  " WHERE Account.id = :userId"
                  " GROUP BY Post.priority").params(userId=userId)
      res = db.engine.execute(statement)

      response = []
      for row in res:
         response.append([row[0], row[1]])

      return response


   @staticmethod
   def count_user_threads(userId):
      statement = text("SELECT COUNT(*) FROM Account"
                  " LEFT JOIN Post ON Account.id = Post.account_id"
                  " WHERE Post.priority = 1 AND Account.id = :userId").params(userId=userId)
      res = db.engine.execute(statement)

      for row in res:
         response = row[0]
      return response


   @staticmethod
   def count_user_posts(userId):
      statement = text("SELECT COUNT(*) FROM Account"
                  " LEFT JOIN Post ON Account.id = Post.account_id"
                  " WHERE Account.id = :userId").params(userId=userId)
      res = db.engine.execute(statement)

      for row in res:
         response = row[0]
      return response


   @staticmethod
   def user_post_ids(userId):
      statement = text("SELECT Post.id, Post.message FROM Account"
                  " LEFT JOIN Post ON Account.id = Post.account_id"
                  " WHERE Account.id = :userId").params(userId=userId)
      res = db.engine.execute(statement)

      response = []
      for row in res:
         response.append(row[0])

      return response


   @staticmethod
   def total_users():
      statement = text("SELECT COUNT(*) FROM Account")
      res = db.engine.execute(statement)

      for row in res:
         response = row[0]
      return response













