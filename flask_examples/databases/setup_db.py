from inde import db, Puppy

# Creates all the table by transforming models into tables.
db.create_all()

sam = Puppy(name = 'Sammy', age = 3)
spot = Puppy(name = 'Spot', age = 1)

print(sam.id)
print(spot.id)

db.session.add_all([sam, spot])

db.session.commit();

print(sam.id)
print(spot.id)
