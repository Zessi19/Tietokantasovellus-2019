from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_manager, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm, ChangeNameForm, ChangeUsernameForm, ChangePasswordForm
from application.posts.models import Post

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
@login_required()
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

   dbUser = User(form.name.data, form.username.data, form.password.data, "USER")
   db.session.add(dbUser)
   db.session.commit()

   return redirect(url_for("auth_login"))


# ---------------------------------
#   User Information and Updating
# ---------------------------------

@app.route("/auth/userinfo", methods=["GET"])
@login_required()
def auth_userinfo():
   countUserThreads = User.count_user_threads(current_user.id) 
   countUserPosts = User.count_user_posts(current_user.id)

   return render_template("auth/userinfo.html", countUserThreads=countUserThreads, countUserPosts=countUserPosts)


@app.route("/auth/changeName", methods=["GET", "POST"])
@login_required()
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
@login_required()
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
@login_required()
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


# ---------------
#   Remove User
# ---------------

@app.route("/auth/removeUser", methods=["POST"])
@login_required(roles=["USER", "ADMIN"])
def auth_remove():
   delete_user_posts(current_user.id)

   dbUser = User.query.get(current_user.id)
   logout_user()

   db.session().delete(dbUser)
   db.session().commit()         
   return redirect(url_for("threads_index"))

# Deletes all post from User(userID)
def delete_user_posts(userId):
   userPosts = User.user_post_ids(userId)

   if userPosts[0] is not None:
      for i in userPosts:
         dbPost = Post.query.get(i)
         db.session().delete(dbPost)
      db.session().commit()


# ----------------------------------
#   ADMIN & MASTER: List All Users
# ----------------------------------

@app.route("/auth/listUsers", methods=["GET"])
@login_required(roles=["ADMIN", "MASTER"])
def auth_list_users():
   if current_user.userrole == "MASTER":
      userList = User.list_users_and_admins()

   if current_user.userrole == "ADMIN":
      userList = User.list_users()

   return render_template("/auth/userList.html", userList=userList)


# ------------------------------------
#   ADMIN & MASTER: Sudo Remove User
# ------------------------------------

@app.route("/auth/sudoRemoveUser/<userId>", methods=["POST"])
@login_required(roles=["ADMIN", "MASTER"])
def auth_sudo_remove_user(userId):
   dbUser = User.query.get(userId)   

   if dbUser.userrole == "MASTER":
      return login_manager.unauthorized()

   if dbUser.userrole == "ADMIN" and current_user.userrole != "MASTER":
      return login_manager.unauthorized()

   # User Posts
   delete_user_posts(userId)

   # User Account
   db.session().delete(dbUser)
   db.session().commit()

   return redirect(url_for("auth_list_users"))


# ----------------------------------------------
#   MASTER: Change User Status (USER vs ADMIN)
# ----------------------------------------------

@app.route("/auth/changeUserStatus/<userId>", methods=["POST"])
@login_required(roles=["MASTER"])
def auth_change_user_status(userId):
   dbUser = User.query.get(userId)   

   if (dbUser.userrole == "USER"):
      dbUser.userrole = "ADMIN"
   else:
      dbUser.userrole = "USER"

   db.session().commit()
   return redirect(url_for("auth_list_users"))





