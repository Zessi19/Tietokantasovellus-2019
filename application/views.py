from flask import render_template
from application import app

from application.auth.models import User
from application.threads.models import Thread
from application.posts.models import Post

@app.route("/")
def index():
   countUsers = User.total_users()
   countThreads = Thread.total_threads()
   countPosts = Post.total_posts()

   return render_template("index.html", countUsers=countUsers, countThreads=countThreads, countPosts=countPosts)
