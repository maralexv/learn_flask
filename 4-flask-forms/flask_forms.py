from flask import Flask, render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,  
					RadioField, SelectField, TextField, TextAreaField, 
					SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


class MyForm(FlaskForm):

	breed = StringField('Whatbreed are you?', validators=[DataRequired()])
	neutered = BooleanField('Have you been neutered?')
	mood = RadioField('Please indicate your mood:',
						choices=[('happy_mood', 'Happy'), ('excited_mood', 'Excited')])
	food = SelectField('Pick your favorite food:', 
						choices=[('bf', 'Beef'), ('prk', 'Pork'), ('vg', 'Vegetables')],
						validators=[DataRequired()])
	feedback = TextAreaField()
	submit = SubmitField('Submit')


@app.route('/', methods = ['GET', 'POST'])
def index():
	form = MyForm()
	if form.validate_on_submit():
		session['breed'] = form.breed.data
		session['neutered'] = form.neutered.data
		session['mood'] = form.mood.data
		session['food'] = form.food.data
		session['feedback'] = form.feedback.data
		return redirect(url_for('thankyou'))
	return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)