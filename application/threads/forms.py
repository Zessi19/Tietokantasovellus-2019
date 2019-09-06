from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, FieldList, FormField, BooleanField, validators
from wtforms.widgets import TextArea


class ThreadForm(FlaskForm):
   topic = StringField("Otsikko:", [validators.Length(min=2, max=100)])
   message = TextAreaField("Viesti:", [validators.Length(min=2, max=4000)], widget=TextArea())

   yleinen = BooleanField("Yleinen", [validators.Optional()])
   retro = BooleanField("Retro", [validators.Optional()])
   wii = BooleanField("Wii", [validators.Optional()])
   wiiu = BooleanField("WiiU", [validators.Optional()])
   switch = BooleanField("Switch", [validators.Optional()])
   ds = BooleanField("DS", [validators.Optional()])
   threeDs = BooleanField("3DS", [validators.Optional()])

   class Meta:
      csrf = False

   # Check that atleast 1 BooleanField filled
   def validate(self):
      if not super(ThreadForm, self).validate():
         return False

      if not self.yleinen.data and not self.retro.data and not self.wii.data and not self.wiiu.data \
         and not self.switch.data and not self.ds.data and not self.threeDs.data:

         self.yleinen.errors.append("Valitse vähintään yksi alue")
         return False
      return True


class ChangeTopicForm(FlaskForm):
   topic = StringField("Otsikko:", [validators.Length(min=2, max=100)])

   class Meta:
      csrf = False
