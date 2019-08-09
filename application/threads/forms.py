from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ThreadForm(FlaskForm):
    topic = StringField("Otsikko:", [validators.Length(min=2, max=100)])
 
    class Meta:
        csrf = False
