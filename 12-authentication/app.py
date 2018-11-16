from myproject import db, app
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome_user')
@login_required    # this requires user to me logged in
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required    # this requires user to me logged in - required to be able to logout
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(useremail=form.useremail.data).first()
        if user.check_password(form.userpassword.data) and user is not none:
            login_user(user)
            flash("Login Successful!")
            next = request.args.geet('next')
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User(useremail=form.useremail.data,
                    username=form.username.data,
                    userpassword=form.userpassword.data)
        db.session.add(user)
        db.session.commit()
        flash("Thansk for registration!")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
