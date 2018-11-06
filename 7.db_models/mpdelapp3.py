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
			return f"{self.id}-name: {self.name} | owner: {self.owner.name}; "
		else:
			return f"{self.id}-name: {self.name} | has no owner; "

	def reprot_toys(self):
		print("Here are my toys:")
		for toy in self.toys:
			print (toy.itemname)


class Toy(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	itemname = db.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey('Puppy.id'))

	def __init__(self, itemname, puppy_id):
		self.itemname = itemname
		self.puppy_id = puppy_id


	def __repr__(self):
		return f"{self.id}-{self.itemname} ;"


class Owner(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	name = bd.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey('Puppy.id'))


	def __init__(self, name, puppy_id):
		self.name = name
		self.puppy_id = puppy_id


	def __repr__(self):
		return f"{self.id}-{self.name} ;"



if __name__=='__main__':
	app.run(debug=True)
