from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods=["GET","POST"])
def auth_login():
   if request.method == "GET":
      return render_template("auth/loginform.html", form=LoginForm())

   form = LoginForm(request.form)
   # mahdolliset validoinnit

   user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
   if not user:
      return render_template("auth/loginform.html", form=form, error="Väärä käyttäjätunnus tai salasana")

   login_user(user)
   return redirect(url_for("threads_index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("threads_index"))


@app.route("/auth/register", methods=["GET","POST"])
def auth_register():
   if request.method == "GET":
      return render_template("auth/register.html", form=RegisterForm())

   form = RegisterForm(request.form)

   if not form.validate():
      return render_template("auth/register.html", form=form)

   dbUser = User(form.name.data, form.username.data, form.password.data, True)
   db.session.add(dbUser)
   db.session.commit()

   return redirect(url_for("auth_login"))   
