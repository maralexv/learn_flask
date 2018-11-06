from modelapp import db, MyDB

db.create_all()

# create data objects to be addede to the db:
sam = MyDB('Sammual', 12)
ted = MyDB('Teddy', 15)
sinty = MyDB('Sinta', 13)
bea = MyDB('Beatris', 14)

# print(sam.id) # None
# print(ted.id) # None
# print(bea.id) # None

# add data objects to the db:
db.session.add_all([sam, ted, sinty, bea])

# another way to add data objects to db:
# db.session.add(sam)
# db.session.add(ted)
# dbsessi0on.add(sinty)
# db.session.add(bea)

# save changes to the db:
db.session.commit()

# print(sam.id)
# print(ted.id)
# print(bea.id) 

