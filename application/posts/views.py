from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post

# ---------------
#   Remove Post
# ---------------

@app.route("/posts/<threadId>/<postId>/remove", methods=["POST"])
def posts_remove(postId, threadId):

   dbPost = Post.query.get(postId)
   db.session().delete(dbPost)
   db.session().commit()

   return redirect(url_for("threads_open", threadId=threadId))
