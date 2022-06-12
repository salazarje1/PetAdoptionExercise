from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()


# Delete Old data
Pet.query.delete()

# Add sample data
pet1 = Pet(name='Rocky', species='dog', photo_url='https://images.unsplash.com/photo-1568572933382-74d440642117?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80', age=5, available=True)

db.session.add(pet1)
db.session.commit()