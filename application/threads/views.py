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
   
   # List: [0] Account.username, [1] Thread.id, [2] Thread.topic, [3] Thread.created, [4] Thread.modified 
   threadData = Thread.get_single_thread(threadId)

   # List:
   postsData = Post.get_posts_in_thread(threadId)   

   ## HTML sivu jossa Username + Topic
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
   dbThread.account_id = current_user.id
   db.session().add(dbThread)
   db.session().flush()

   dbPost = Post(form.message.data)
   dbPost.account_id = current_user.id
   dbPost.thread_id = dbThread.id
   db.session().add(dbPost)

   db.session().commit()
   return redirect(url_for("threads_index"))


# -----------------------
#   Change Thread Topic
# -----------------------

@app.route("/threads/<threadId>/update", methods=["GET", "POST"])
def threads_update(threadId):
   oldTopic = Thread.query.get(threadId).topic

   if request.method == "GET":
      return render_template("threads/update.html", form=ChangeTopicForm(), threadId=threadId, oldTopic=oldTopic)

   form = ChangeTopicForm(request.form)
   if not form.validate():
      return render_template("threads/update.html", form=form, threadId=threadId, oldTopic=oldTopic)

   dbThread = Thread.query.get(threadId)
   dbThread.topic = form.topic.data
   db.session().commit()

   return redirect(url_for("threads_index"))


# -----------------
#   Remove Thread    ### LISÄÄ KAIKKIEN KETJUN POST:ien POISTO ###
# -----------------

@app.route("/threads/<threadId>/remove", methods=["POST"])
def threads_remove(threadId):

   dbThread = Thread.query.get(threadId)
   db.session().delete(dbThread)
   db.session().commit()

   return redirect(url_for("threads_index"))





