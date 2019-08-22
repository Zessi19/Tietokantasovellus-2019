from flask_wtf import FlaskForm

from wtforms import TextAreaField, validators
from wtforms.widgets import TextArea


class PostForm(FlaskForm):
   message = TextAreaField("Viesti:", [validators.Length(min=2, max=4000)], widget=TextArea())

   class Meta:
      csrf = False
