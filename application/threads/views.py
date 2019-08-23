from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.threads.forms import ThreadForm, ChangeTopicForm
from application.posts.models import Post

# --------------------
#   List All Threads
# --------------------

@app.route("/threads", methods=["GET"])
def threads_index():
   threadList = Thread.query.all()
   return render_template("threads/list.html", threadList=threadList)


# ---------------
#   View Thread
# ---------------

@app.route("/threads/<threadId>/open", methods=["GET"])
def threads_open(threadId):
 
   # List(4 elements): [0] Thread.id, [1] Thread.topic, [2] Thread.created, [3] Thread.modified
   threadData = Thread.get_thread(threadId)

   # List of list(5 elements): [0] Account.username, [1] Post.id, [2] Post.message, [3] Post.created, [4] Post.modified
   postsData = Post.get_posts_in_thread(threadId)

   return render_template("threads/open.html", threadData=threadData, postsData=postsData)


# ---------------------
#   Create New Thread
# ---------------------

@app.route("/threads/new", methods=["GET", "POST"])
@login_required
def threads_create():
   if request.method == "GET":
      return render_template("threads/new.html", form=ThreadForm())

   form = ThreadForm(request.form)
   if not form.validate():
      return render_template("threads/new.html", form=form)

   dbThread = Thread(form.topic.data)
   db.session().add(dbThread)
   db.session().flush()

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
def threads_remove(threadId):
   postsData = Post.get_posts_in_thread(threadId)
   
   for row in postsData:
      dbPost = Post.query.get(row[1])
      db.session().delete(dbPost)

   dbThread = Thread.query.get(threadId)
   db.session().delete(dbThread)

   db.session().commit()
   return redirect(url_for("threads_index"))





