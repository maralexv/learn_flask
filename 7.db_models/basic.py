# BASIC.PY
# Place where we shall create entries in the tables

from model3 import db, Puppy, Toy, Owner

# CREATE 2 PUPPIES
moses = Puppy('Moses')
fido = Puppy('Fido')
# ADD PUPPIES TO DB
db.session.add_all([moses, fido])
db.session.commit()

# CHECK IT!
print(Puppy.query.all())

# GRAP A PUPPY
moses = Puppy.query.filter_by(name='Moses').first() # .first methd grabs the first item, satisfying the condition of .filter method
print(moses)

# CREATE OWNER OBJECT
alex = Owner('Alex', moses.id) # moses.id -- here the .id methid grabs the id of the puppy form the puppies table

# GIVE MOSES SOME toys
toy1 = Toy('Plastic bown', moses.id)
toy2 = Toy('Ball', moses.id)

db.session.add_all([alex, toy1, toy2])
db.session.commit()

# GRAP OUR PUPPY AFTER ALL THOSE CHANGES
moses = Puppy.query.filter_by(name='Moses').first()
print(moses)

print([toy1, toy2])
