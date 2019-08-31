from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, FieldList, FormField, BooleanField, validators
from wtforms.widgets import TextArea


class ThreadForm(FlaskForm):
   topic = StringField("Otsikko:", [validators.Length(min=2, max=100)])
   message = TextAreaField("Viesti:", [validators.Length(min=2, max=4000)], widget=TextArea())

   yleinen = BooleanField("Yleinen")
   retro = BooleanField("Retro")
   wii = BooleanField("Wii")
   wiiu = BooleanField("Wii U")
   switch = BooleanField("Switch")
   ds = BooleanField("DS")
   threeDs = BooleanField("3DS")

   class Meta:
      csrf = False


class ChangeTopicForm(FlaskForm):
   topic = StringField("Otsikko:", [validators.Length(min=2, max=100)])

   class Meta:
      csrf = False
