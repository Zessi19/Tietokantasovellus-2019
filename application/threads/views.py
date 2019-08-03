from application import app, db
from flask import redirect, render_template, request, url_for
from application.threads.models import Thread

@app.route("/threads", methods=["GET"])
def threads_index():
   return render_template("threads/list.html", threads=Thread.query.all())


@app.route("/threads", methods=["POST"])
def threads_create():
   thread_db = Thread(request.form.get("subject"))

   db.session().add(thread_db)
   db.session().commit()
   return redirect(url_for("threads_index"))


@app.route("/threads/new")
def threads_form():
   return render_template("threads/new.html")

@app.route("/threads/<thread_id>", methods=["POST"])
def threads_update(thread_id):
   thread_db = Thread.query.get(thread_id)
   thread_db.subject = request.form.get("new_subject")
   db.session().commit()
   return redirect(url_for("threads_index"))
