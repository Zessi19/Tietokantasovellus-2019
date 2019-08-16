from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from wtforms.widgets import PasswordInput

from application.auth.models import User
 
class LoginForm(FlaskForm):
   username = StringField("Käyttäjätunnus:")
   password = PasswordField("Salasana:")
  
   class Meta:
      csrf = False


class RegisterForm(FlaskForm):
   name = StringField("Nimi:", [validators.Length(min=2, max=50)])
   username = StringField("Käyttäjätunnus:", [validators.Length(min=2, max=20)])
   password = PasswordField("Salasana:", [validators.Length(min=8, max=50), 
      validators.EqualTo('confirm', message='Salasanat eivät täsmää')])
   confirm = PasswordField("Toista Salasana:")

   def validate_username(self, field):
      if User.query.filter_by(username=field.data).first():
         raise ValidationError('Käyttäjätunnus on jo käytössä')
   class Meta:
      csrf = False


class ChangeNameForm(FlaskForm):
   name = StringField("Nimi:", [validators.Length(min=2, max=50)])

   class Meta:
      csrf = False


class ChangeUsernameForm(FlaskForm):
   username = StringField("Käyttäjätunnus:", [validators.Length(min=2, max=20)])

   def validate_username(self, field):
      if User.query.filter_by(username=field.data).first():
         raise ValidationError('Käyttäjätunnus on jo käytössä')
   class Meta:
      csrf = False


class ChangePasswordForm(FlaskForm):
   password = PasswordField("Salasana:", [validators.Length(min=8, max=50),
      validators.EqualTo('confirm', message='Salasanat eivät täsmää')], widget=PasswordInput(hide_value=False))
   confirm = PasswordField("Toista Salasana:", widget=PasswordInput(hide_value=False))

   class Meta:
      csrf = False





