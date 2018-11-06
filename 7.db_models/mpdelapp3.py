# MODELAPP3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.cofig['SQLALCHEMY_DATABASE_URI'] = 'sqlite///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Puppy(db.Model):

	id = db.Column(db.Ineger, primary_key=True)
	name = db.Column(db.Text)
	# Connecting puppies and toys (Puppy Model to Toy Model) - ONE TO MANY
	toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
	# Connecting puppies to owners (Puppy Model to Owner Model)  - ONE TO ONE
	owner = db.relationship('Owner', backref='puppy', uselist=False)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		if self.owner:
			return f"{self.id}| name: {self.name} | owner: {self.owner.name}; "
		else:
			return f"{self.id}| name: {self.name} | has no owner; "

	def reprot_toys(self):
		print("Here are my toys:")
		for toy in self.toys:
			print (toy.itemname)


class Toy(db.Model):
	pass

class Owner(db.Model):
	pass





if __name__=='__main__':
	app.run(debug=True)
