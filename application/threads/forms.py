from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, validators
from wtforms.widgets import TextArea

class ThreadForm(FlaskForm):
   topic = StringField("Otsikko:", [validators.Length(min=2, max=100)])
   message = TextAreaField("Viesti:", [validators.Length(min=2, max=4000)], widget=TextArea())

   class Meta:
      csrf = False



class ChangeTopicForm(FlaskForm):
   topic = StringField("Otsikko:", [validators.Length(min=2, max=100)])

   class Meta:
      csrf = False
