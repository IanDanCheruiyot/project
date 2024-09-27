from models import session, Cow, LactationRecord, Employee, Customer, SalesRecord
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add Cow
def add_cow():
    name = input("Enter cow's name: ").strip()
    breed = input("Enter cow's breed: ").strip()

    if not name or not breed:
        print("Name and breed are required.")
        return
    
    cow = Cow(name=name, breed=breed)
    session.add(cow)
    session.commit()
    print(f"Cow '{name}' added successfully!")

# View All Cows
def view_all_cows():
    cows = session.query(Cow).all()
    if cows:
        for cow in cows:
            print(f"ID: {cow.id}, Name: {cow.name}, Breed: {cow.breed}")
    else:
        print("No cows found!")