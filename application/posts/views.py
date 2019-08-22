from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post
from application.posts.forms import PostForm

# ---------------
#   New Post
# ---------------

@app.route("/posts/<threadId>/new", methods=["GET", "POST"])
@login_required
def posts_new(threadId):
   if request.method == "GET":
      return render_template("posts/new.html", form=PostForm(), threadId=threadId)

   form = PostForm(request.form)
   if not form.validate():
      return render_template("posts/new.html", form=form)

   dbPost = Post(form.message.data, 0)
   dbPost.account_id = current_user.id
   dbPost.thread_id = threadId

   db.session().add(dbPost)
   db.session().commit()
   return redirect(url_for("threads_open", threadId=threadId))


# ---------------
#   Update Post
# ---------------

@app.route("/posts/<threadId>/<postId>/update", methods=["GET", "POST"])
def posts_update(threadId, postId):
   dbPost = Post.query.get(postId)

   if request.method == "GET":
      form = PostForm()
      form.message.data = dbPost.message
      return render_template("posts/update.html", form=form, threadId=threadId, postId=postId)

   form = PostForm(request.form)
   if not form.validate():
      return render_template("posts/update.html", form=form, threadId=threadId, postId=postId)

   dbPost.message = form.message.data
   db.session().commit()
   return redirect(url_for("threads_open", threadId=threadId))


# ---------------
#   Remove Post
# ---------------

@app.route("/posts/<threadId>/<postId>/remove", methods=["POST"])
def posts_remove(threadId, postId):

   dbPost = Post.query.get(postId)
   db.session().delete(dbPost)
   db.session().commit()

   return redirect(url_for("threads_open", threadId=threadId))
