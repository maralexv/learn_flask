from flask import Flask, render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,  
						RadioField, SelectField, TextField, TextAreaField, 
						SubmitField)
from wtfforms.validators import DataRequired

app = Flask(__name__)
app.config[SECRET_KEY] = 'mysecretkey:augq;.jhciafgjw?><WKB'


class MyForm(FlaskForm):

	breed = StringField('Whatbreed are you?', validators=[DataRequired()])
	neutered = BooleanField('Have you been neutered?')
	mood = RadioField('Please indicate your mood:',
						choices=[('mood1', 'Happy'), ('mood2', 'Excited')])
	food = SelectField('Pick your favorite food:', 
						choices=[('bf', 'Beef'), ('prk', 'Pork'), ('vg', 'Vegetables')]
	feedback = TextAreaField()
	submit = SubmitField('Submit')



@app.route('/', methods = ['GET', 'POST'])
def index():
	form = MyForm()
	if form.validate_on_submit();



	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)