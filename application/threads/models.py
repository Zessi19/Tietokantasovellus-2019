from application import db
from application.models import Base

from sqlalchemy.sql import text


class Thread(Base):
   topic = db.Column(db.String(100), nullable=False)
#   account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

   def __init__(self, topic):
      self.topic = topic


   @staticmethod
   def get_single_thread(threadId):
      statement = text("SELECT Account.username, Thread.id, Thread.topic, Thread.created, Thread.modified FROM Thread"
                  " LEFT JOIN Account ON Account.id = Thread.account_id"
                  " WHERE Thread.id = :threadId").params(threadId=threadId)
      res = db.engine.execute(statement)
 
      response = [] 
      for row in res:
         response.append(row[0]); response.append(row[1]);
         response.append(row[2]); response.append(row[3]); response.append(row[4]);

      return response

