from index import db, Puppy

# Create a new entry.
rufus = Puppy(name = 'Rufus', age = 5)
db.session.add(rufus)
db.session.commit()

# Read all puppies in table.
all = Puppy.query.all()
print(all)

puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# Filter
# Produces some sql code.
puppy_spot = Puppy.query.filter_by(name = 'spot')
print(puppy_spot.all())

# Update
puppy_one.age = 10
db.session.add(puppy_one)
db.session.commit()

# Delete
puppy_two = Puppy.query.get(2)
db.session.delete(puppy_two)
db.session.commit()
