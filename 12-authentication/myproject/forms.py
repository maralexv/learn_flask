from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Email,EqualTo, Length
from wtforms import ValidationError


class LoginForm(FlaskForm):
    useremail = StringField('Email: ', validators = [DataRequired(), Email()])
    userpassword = PasswordField('Password: ', validators = [DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    useremail = StringField('Email: ', validators = [DataRequired(), Email()])
    username = StringField('Username: ', validators = [DataRequired(), Length(min=4)])
    userpassword = PasswordField('Password: ', validators = [DataRequired(), EqualTo('passconfirm', message='Please make sure your passwords match.'), Length(min=8)])
    passconfirm = PasswordField('Confirm password: ', validators = [DataRequired(), Length(min=8)])
    tnc = BooleanField('Agree to terms and conditions.', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_useremail(self, field):
        if User.query.filter_by(useremail=field.data).first():
            raise ValidationError('A user with such email already exists.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Such username is already talen.')
