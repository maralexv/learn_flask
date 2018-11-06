import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# CONNECTING DATABASE TO THE APP
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

	def __init__(self, name, age):
		
		self.name = name
		self.age = age

	def __repr__(self):
		return f"ID={self.id}, name={self.name}, age={self.age}"


if __name__ == '__main__':
    app.run()