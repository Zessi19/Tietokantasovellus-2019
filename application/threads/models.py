from application import db
from application.models import Base

from sqlalchemy.sql import text

# --------------------
#    ThreadCategory
# --------------------

threadcategory = db.Table("threadcategory",
   db.Column("thread_id", db.Integer, db.ForeignKey("thread.id"), primary_key=True),
   db.Column("category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True)
)


# --------------
#     Thread 
# --------------

class Thread(Base):
   topic = db.Column(db.String(100), nullable=False)
   posts = db.relationship("Post", backref='thread', lazy=True)
   categories = db.relationship("Category", secondary=threadcategory, backref=db.backref("threads"), lazy=True)

   def __init__(self, topic):
      self.topic = topic


   @staticmethod
   def get_thread(threadId):
      statement = text("SELECT Thread.id, Thread.topic, Thread.created, Thread.modified FROM Thread"
                  " WHERE Thread.id = :threadId").params(threadId=threadId)
      res = db.engine.execute(statement)
 
      response = [] 
      for row in res:
         response.append(row[0]); response.append(row[1]);
         response.append(row[2]); response.append(row[3]);

      return response


   @staticmethod
   def get_default_threadList():
      statement = text("SELECT Thread.id, Thread.topic, Category.name FROM Thread"
                  " LEFT JOIN ThreadCategory ON Thread.id = ThreadCategory.thread_id"
                  " LEFT JOIN Category ON ThreadCategory.category_id = Category.id"
                  " ORDER BY Thread.id ASC")
      res = db.engine.execute(statement)

      response = []
      categories = []
      oldId = None
      oldTopic = None

      for row in res:
         if (row[0] != oldId and oldId is not None):
            response.append([oldId, oldTopic, categories])    
            categories = []

         categories.append(row[2])
         oldId = row[0]
         oldTopic = row[1]

      response.append([oldId, oldTopic, categories])
      return response


   @staticmethod
   def total_threads():
      statement = text("SELECT COUNT(*) FROM Thread")
      res = db.engine.execute(statement)

      for row in res:
         response = row[0]
      return response


# ----------------
#     Category 
# ----------------

class Category(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255), nullable=False)

   def __init__(self, name):
      self.name = name




