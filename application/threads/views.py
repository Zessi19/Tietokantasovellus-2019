from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.threads.models import Thread, Category
from application.threads.forms import ThreadForm, ChangeTopicForm
from application.posts.models import Post

# --------------------
#   List All Threads
# --------------------

@app.route("/threads", methods=["GET"])
def threads_index():

   #List of lists(3 elements): [0] Thread.id, [1] Thread.topic, [2] List of Category names
   threadList = Thread.get_default_threadList()

   return render_template("threads/list.html", threadList=threadList)


# ---------------
#   Open Thread
# ---------------

@app.route("/threads/<threadId>/open", methods=["GET"])
def threads_open(threadId):

   # List(4 elements): [0] Thread.id, [1] Thread.topic, [2] Thread.created, [3] Thread.modified
   threadData = Thread.get_thread(threadId)

   # List of list(6 elements): [0] Account.id, [1] Account.username, [2] Post.id, [3] Post.message, [4] Post.created, [5] Post.modified
   postsData = Post.get_posts_in_thread(threadId)

   return render_template("threads/open.html", threadData=threadData, postsData=postsData)


# ---------------------
#   Create New Thread
# ---------------------

@app.route("/threads/new", methods=["GET", "POST"])
@login_required()
def threads_create():
   if request.method == "GET":
      return render_template("threads/new.html", form=ThreadForm())

   form = ThreadForm(request.form)
   if not form.validate():
      return render_template("threads/new.html", form=form)

   dbThread = Thread(form.topic.data)
   db.session().add(dbThread)
   db.session().flush()

   if (form.yleinen.data == True):
      dbCategory = Category.query.filter_by(name="Yleinen").first()
      dbThread.categories.append(dbCategory)
      
   if (form.retro.data == True):
      dbCategory = Category.query.filter_by(name="Retro").first()
      dbThread.categories.append(dbCategory)

   if (form.wii.data == True):
      dbCategory = Category.query.filter_by(name="Wii").first()
      dbThread.categories.append(dbCategory)

   if (form.wiiu.data == True):
      dbCategory = Category.query.filter_by(name="Wii U").first()
      dbThread.categories.append(dbCategory)

   if (form.switch.data == True):
      dbCategory = Category.query.filter_by(name="Switch").first()
      dbThread.categories.append(dbCategory)

   if (form.ds.data == True):
      dbCategory = Category.query.filter_by(name="DS").first()
      dbThread.categories.append(dbCategory)

   if (form.threeDs.data == True):
      dbCategory = Category.query.filter_by(name="3DS").first()
      dbThread.categories.append(dbCategory)



   dbPost = Post(form.message.data, 1)
   dbPost.account_id = current_user.id
   dbPost.thread_id = dbThread.id
   db.session().add(dbPost)

   db.session().commit()
   return redirect(url_for("threads_index"))


# -----------------------
#   Update Thread Topic
# -----------------------

@app.route("/threads/<threadId>/update", methods=["GET", "POST"])
@login_required(roles=["ADMIN","MASTER"])
def threads_update(threadId):
   dbThread = Thread.query.get(threadId)

   if request.method == "GET":
      form = ChangeTopicForm()
      form.topic.data = dbThread.topic
      return render_template("threads/update.html", form=form, threadId=threadId)

   form = ChangeTopicForm(request.form)
   if not form.validate():
      return render_template("threads/update.html", form=form, threadId=threadId)

   dbThread.topic = form.topic.data
   db.session().commit()
   return redirect(url_for("threads_index"))


# -----------------
#   Remove Thread  
# -----------------

@app.route("/threads/<threadId>/remove", methods=["POST"])
@login_required(roles=["ADMIN","MASTER"])
def threads_remove(threadId):
   postsData = Post.get_posts_in_thread(threadId)
   
   for row in postsData:
      dbPost = Post.query.get(row[1])
      db.session().delete(dbPost)

   dbThread = Thread.query.get(threadId)
   db.session().delete(dbThread)

   db.session().commit()
   return redirect(url_for("threads_index"))




