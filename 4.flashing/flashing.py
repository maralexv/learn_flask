from flask import Flask, render_template, session, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lrigq)(*$&(*^lejkfba?<aygbe'

class SimpleForm(FlaskForm):

	breed = StringField('WHat breed are you?')
	submit = SubmitField('Click Me')


@app.route('/', methods=['GET', 'POST'])
def index():

	form = SimpleForm()

	if form.validate_on_submit():
		session['breed'] = form.breed.data
		flash(f"You just changed your {session['breed']}")
		return redirect(url_for('index'))

	return render_template('index.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)

