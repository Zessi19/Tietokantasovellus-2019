from flask import render_template

from application import app
from application.threads.models import Thread
from application.posts.models import Post

@app.route("/")
def index():
   countThreads = Thread.total_threads()
   countPosts = Post.total_posts()  
   return render_template("index.html", countThreads=countThreads, countPosts=countPosts)
