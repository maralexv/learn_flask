#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class  AddForm(FlaskForm):

    name = StringField('Name of the Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('ID of the Puppy to remove: ')
    submit = SubmitField('Remove Puppy')
    
