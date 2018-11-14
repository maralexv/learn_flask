# adoption_site.py
import os
from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, \
                    redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd\2_4t#:-y1p9FqrHg0c/n><A9qrb'

################################
##### SQL DATABASE SECTION #####
################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

################################
#####        MODELS        #####
################################

class Puppy(db.Model):

    __tablename__ = 'pups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # Connecting puppies to owners (Puppy Model to Owner Model)  - ONE TO ONE
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy: {self.name} has Owner {self.owner.name}."
        else:
            return f"Puppy: {self.name} has no owner :-("


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    pup_id = db.Column(db.Integer, db.ForeignKey('pups.id'))

    def __init__(self, name, pup_id):
        self.name = name
        self.pup_id = pup_id

        def __repr__(self):
            return f"Owner {self.name}."

#######################################################
####  VIEW FUNCTIONS (WEB PAGES, SOME WITH FOMRS)  ####
#######################################################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods = ['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)

@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods = ['GET', 'POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)


@app.route('/addowner', methods = ['GET', 'POST'])
def add_owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        name = form.name.data
        owner = Owner(name, pup.id)
        db.session.add(owner)
        db.session.commit()
        flash(f"You have successfully added {name} to our Owners DataBase.")
        return redirect(url_for('list_pup'))
    return render_template('addowner.html', form=form)


if __name__ == '__main__':
    app.run (debug=True)
