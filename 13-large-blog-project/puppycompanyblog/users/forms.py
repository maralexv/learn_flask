from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Email, DataRequired, EqualTo, Length
from flask_wtf import FileField, FileAllowed 

from flask_login import current_user
from puppycompanyblog.models import User


class LoginForm(FlaskForm):
	useremail = StringField('Email', validators=[DataRequired(), Email()])
	userpassword = StringField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')



class RegistrationForm(FlaskForm):
	useremail = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('UserName', validators=[DataRequired(), Length(min=4)])
	userpassword = PasswordField('Password', validators=[DataRequired(), Length(min=8), EqualTo('userpass_confirm', message='Paswords must match.')])
	userpass_confirm = PasswordField('Confirm Password', validators=[DataRequired(), ])
	submit = SubmitField('Register')


	def check_useremail(self, field):
		if User.query.filter_by(useremail=field.data).first():
			raise ValidationError("This email address has been registered already.")


	def check_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError("This username has been registered already.")



class UpdateUserForm(FlaskForm):
	useremail = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('UserName', validators=[DataRequired(), Length(min=4)])
	profile_image = FileField('Uplod Profile Picture', validators=[FileAllowed([jpg, png, jpeg, tiff, gif, bmp])])
	submit = SubmitField('Update User Profile')


	def check_useremail(self, field):
		if User.query.filter_by(useremail=field.data).first():
			raise ValidationError("This email address has been registered already.")


	def check_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError("This username has been registered already.")
