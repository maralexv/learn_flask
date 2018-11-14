# views.py under 'owners' dir
from flask import Blueprint, render_template, redirect, url_for, flash
from project import db
from project.models import Owner
from project.owners.forms import AddOForm

owners_blueprint = Blueprint('owners', __name__, template_folder = 'templates/owners')


@owners_blueprint.route('/add', methods = ['GET', 'POST'])
def add():
    form = AddOForm()
    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data
        # add new owner to the db
        owner = Owner(name, id)
        db.session.add(owner)
        db.session.commit()
        flash(f"You have successfully added {name} to our Owners DataBase.")
        return redirect(url_for('puppies.list'))
    return render_template('add.html', form=form)
