# forms.py under 'owners' dir

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Name of the Owner: ")
    id = IntegerField ("ID of the Puppy to adopt: ")
    submit = SubmitField ("Add Owner")
