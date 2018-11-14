# views.py under 'owners' dir
from flask import Blueprint, render_template, redirect, url_for, flash
from project import db
from project.models import Owner
from project.owners.forms import AddForm

owners_blueprint = Blueprint('owners', __name__, \
                        tamplate_folder = 'tamplates/owners')


@owners_blueprint.route('/add', methods = ['GET', 'POST'])
def add():
    form = AddOwnerForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        name = form.name.data
        # add new owner to the db
        owner = Owner(name, pup.id)
        db.session.add(owner)
        db.session.commit()
        flash(f"You have successfully added {name} to our Owners DataBase.")
        return redirect(url_for('puppies.list'))
    return render_template('add.html', form=form)
