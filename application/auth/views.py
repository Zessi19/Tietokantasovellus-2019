from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm, ChangeNameForm, ChangeUsernameForm, ChangePasswordForm

# ----------------
#   Login/Logout
# ----------------

@app.route("/auth/login", methods=["GET","POST"])
def auth_login():
   if request.method == "GET":
      return render_template("auth/loginform.html", form=LoginForm())

   form = LoginForm(request.form)
   user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

   if not user:
      return render_template("auth/loginform.html", form=form, error="Väärä käyttäjätunnus tai salasana")

   login_user(user)
   return redirect(url_for("threads_index"))


@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("threads_index"))



# ------------
#   Register 
# ------------
 
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



# ---------------------------------
#   User information and updating
# ---------------------------------

@app.route("/auth/userinfo", methods=["GET"])
@login_required
def auth_userinfo():
   return render_template("auth/userinfo.html")


@app.route("/auth/changeName", methods=["GET", "POST"])
@login_required
def auth_change_name():
   dbUser = User.query.get(current_user.id)

   if request.method == "GET":
      form = ChangeNameForm()
      form.name.data = dbUser.name
      return render_template("auth/changeName.html", form=form)

   form = ChangeNameForm(request.form)
   if not form.validate():
      return render_template("auth/changeName.html", form=form)

   dbUser.name = form.name.data
   db.session().commit()   
   return redirect(url_for("auth_userinfo"))


@app.route("/auth/changeUsername", methods=["GET", "POST"])
@login_required
def auth_change_username():
   dbUser = User.query.get(current_user.id)

   if request.method == "GET":
      form = ChangeUsernameForm()
      form.username.data = dbUser.username
      return render_template("auth/changeUsername.html", form=form)

   form = ChangeUsernameForm(request.form)
   if not form.validate():
      return render_template("auth/changeUsername.html", form=form)

   dbUser.username = form.username.data
   db.session().commit()
   return redirect(url_for("auth_userinfo"))


@app.route("/auth/changePassword", methods=["GET", "POST"])
@login_required
def auth_change_password():
   dbUser = User.query.get(current_user.id)

   if request.method == "GET":
      form = ChangePasswordForm()
      form.password.data = dbUser.password
      form.confirm.data = dbUser.password
      return render_template("auth/changePassword.html", form=form)

   form = ChangePasswordForm(request.form)
   if not form.validate():
      return render_template("auth/changePassword.html", form=form)

   dbUser.password = form.password.data
   db.session().commit()
   return redirect(url_for("auth_userinfo"))



#### KESKEN #####
# ---------------
#   Remove user
# ---------------
@login_required
@app.route("/auth/removeUser", methods=["POST"])
def auth_remove():

   return redirect(url_for("threads_index"))
