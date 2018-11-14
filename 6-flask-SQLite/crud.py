from modelapp import db, MyDB

#### CRUD --> CREATE, READ, UPDATE, DELETE 

##### CREATE ENTRY:

new_entry = MyDB('Alex', 46)
db.session.add(new_entry)
db.session.commit()


##### READ ENTRIES:

all_entries = MyDB.query.all() # this wil be a list of all objects in the db
print(all_entries)

entry2 = MyDB.query.get(2) # gets object with key 2, ...
print(entry2.name) # prints the 'name' of the 1st object (with key 1)
    
x = MyDB.query.filter_by(id=2) # generates SQL Code with given filter parameters
l = x.all()	# produces a list of entries with given parameter (in this case key = 1, same as entry1)
print(l)

y = MyDB.query.filter_by(age=15) # generates SQL Code with given filter parameters
l = y.all()  # produces a list of entries with given parameter (in this case key = 1, same as entry1)
print (l)


##### UPDATE ENTRIES:

entry5 = MyDB.query.get(5) # gets entry (with key 5 in this case)
entry5.age = 6			# change the age (pr other parameter)
db.session.add(entry5)  # add the entry back to the db
db.session.commit()     # save the db



##### DELETE ENTRIES:

entry4 = MyDB.query.get(4) # get the entry(ies) with given parameters (with key 5 in this case)
db.session.delete(entry4) # delete seelected entry(ies)
db.session.commit()			# save the changes

###############################################

# Check the db:
print (MyDB.query.all())



