from models import session, Cow, LactationRecord, Employee, Customer, SalesRecord

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

