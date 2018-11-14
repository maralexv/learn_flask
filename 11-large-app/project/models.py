# MAIN MODELS.PY
from project import db  # db shoukd be set-up inside __init__.py uner 'project' directory

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
