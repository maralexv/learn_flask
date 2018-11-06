import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# CONNECTING DATABASE TO THE APP
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

#################################################

# SETTGIN UP THE DATABASE IN THE APP

class MyDB(db.Model):
	# Mannual overwrite of the Table Name 
	__tablename__ = 'mytable1'

	# Set-up Tabel KEY:
	id = db.Column(db.Integer, primary_key=True)
	# Set-up other columns of the table:
	name = db.Column(db.Text)
	age = db.Column(db.Integer)
	sex = db.Column(db.Text)

	def __init__(self, name, age, sex):
		
		self.name = name
		self.age = age
		self.sex = sex

	def __repr__(self):
		return f"{self.id}|{self.name}|{self.age}|{self.sex}"


if __name__ == '__main__':
    app.run()