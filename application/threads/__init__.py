from application import db
from application.threads.models import Category

from sqlalchemy import event


@event.listens_for(Category.__table__, "after_create")
def insert_initial_values(*args, **kwargs):
   db.session.add(Category("Yleinen"))
   db.session.add(Category("Retro"))

   db.session.add(Category("Wii"))
   db.session.add(Category("Wii U"))
   db.session.add(Category("Switch"))

   db.session.add(Category("DS"))
   db.session.add(Category("3DS"))
   db.session.commit()
