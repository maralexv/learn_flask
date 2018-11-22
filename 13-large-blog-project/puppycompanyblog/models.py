# puppyblogcompany/models.py
from puppyblogcompany import db, login_manager 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


class User(db.Model, UserMixin):
	
	__tablename__ = 'users'

	id = db.Column(de.Integer, primary_key=True)
	profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
	useremail = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	userpassword_hash = db.Column(db.String(128), index=True)

	posts = db.relationship(BlogPost, backref='author', lazy=True)


	def __init__(self, useremail, username, userpassword):
		self.useremail = useremail
		self.username = username
		self.userpassword_hash = generate_password_hash(userpassword)


	def check_password(self, userpassword):
		return check_password_hash(self.userpassword_hash, userpassword)


	def __repr__(self):
		return f"User name :{self.username}."



class BlogPost(db.Model):
	
	__tablename__ = 'blogposts'

	users = db.relationship(User)

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	title = db.Column(db.String, nullable=False)
	text = db.Column(db.Text, nullable=False)

	
	def __init__(self, title, text, username):
		self.title = title
		self.text = text
		self.username = username



	def __repr__(self):
		return f"Post ID: {sef.id} -- Date: {self.date} -- Title: {self.title}."











