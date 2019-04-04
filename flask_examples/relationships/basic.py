from models import db, Puppy, Owner, Toy

db.create_all()

rufus = Puppy('rufus')
spot = Puppy('spot')

db.session.add_all([rufus, spot])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='rufus').first()

jose = Owner('José', rufus.id)
ball_toy = Toy('Ball', rufus.id)
train_toy = Toy('Train', rufus.id)

db.session.add_all([jose, ball_toy, train_toy])
db.session.commit()

rufus = Puppy.query.get(rufus.id)
print(rufus)

rufus.report()