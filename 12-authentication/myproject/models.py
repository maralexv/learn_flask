from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    userid = db.Column(db.Integer, primary_key = True)
    useremail = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    userpassword_hash = db.Column(db.String(128))

    def __init__(self, useremail, username, userpassword):
        self.useremail = useremail
        self.username = username
        self.userpassword_hash = generate_password_hash(userpassword)

    def check_password(self, userpassword):
        self.userpassword = userpassword
        return check_password_hash(self.userpassword_hash, userpassword)
