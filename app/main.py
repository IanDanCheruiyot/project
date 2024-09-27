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

# Delete Cow
def delete_cow():
    cow_id = int(input("Enter cow ID to delete: "))
    cow = session.query(Cow).get(cow_id)

    if cow:
        session.delete(cow)
        session.commit()
        print(f"Cow with ID {cow_id} deleted successfully!")
    else:
        print(f"Cow with ID {cow_id} not found!")

# Add Employee
def add_employee():
    name = input("Enter employee name: ").strip()
    position = input("Enter employee position: ").strip()

    if not name or not position:
        print("Name and position are required.")
        return

    employee = Employee(name=name, position=position)
    session.add(employee)
    session.commit()
    print(f"Employee '{name}' added successfully!")

# View All Employees
def view_all_employees():
    employees = session.query(Employee).all()
    if employees:
        for employee in employees:
            print(f"ID: {employee.id}, Name: {employee.name}, Position: {employee.position}")
    else:
        print("No employees found!")

# Delete Employee
def delete_employee():
    employee_id = int(input("Enter employee ID to delete: "))
    employee = session.query(Employee).get(employee_id)

    if employee:
        session.delete(employee)
        session.commit()
        print(f"Employee with ID {employee_id} deleted successfully!")
    else:
        print(f"Employee with ID {employee_id} not found!")

# Add Lactation Record
def add_lactation_record():
    cow_id = int(input("Enter cow ID: "))
    date = input("Enter record date (YYYY-MM-DD): ").strip()
    milk_produced = float(input("Enter milk produced (liters): "))

    cow = session.query(Cow).get(cow_id)
    if not cow:
        print(f"Cow with ID {cow_id} not found!")
        return

    lactation_record = LactationRecord(date=date, milk_produced=milk_produced, cow=cow)
    session.add(lactation_record)
    session.commit()
    print(f"Lactation record for cow '{cow.name}' added successfully!")

# View All Lactation Records
def view_all_lactation_records():
    records = session.query(LactationRecord).all()
    if records:
        for record in records:
            print(f"ID: {record.id}, Date: {record.date}, Milk Produced: {record.milk_produced}L, Cow: {record.cow.name}")
    else:
        print("No lactation records found!")

# Delete Lactation Record
def delete_lactation_record():
    record_id = int(input("Enter lactation record ID to delete: "))
    record = session.query(LactationRecord).get(record_id)

    if record:
        session.delete(record)
        session.commit()
        print(f"Lactation record with ID {record_id} deleted successfully!")
    else:
        print(f"Lactation record with ID {record_id} not found!")

# Add Customer
def add_customer():
    name = input("Enter customer name: ").strip()
    contact_info = input("Enter customer contact info: ").strip()

    if not name:
        print("Customer name is required.")
        return

    customer = Customer(name=name, contact_info=contact_info)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' added successfully!")

# Generate Sales Record
def generate_sales_record():
    cow_id = int(input("Enter cow ID: "))
    customer_id = int(input("Enter customer ID: "))
    employee_id = int(input("Enter employee ID: "))
    sale_date = input("Enter sale date (YYYY-MM-DD): ")
    quantity_sold = float(input("Enter milk quantity sold (in liters): "))
    price = float(input("Enter sale price (total): "))

    cow = session.query(Cow).get(cow_id)
    customer = session.query(Customer).get(customer_id)
    employee = session.query(Employee).get(employee_id)

    if not cow or not customer or not employee:
        print("Invalid cow, customer, or employee ID.")
        return

    sale = SalesRecord(sale_date=sale_date, quantity_sold=quantity_sold, price=price,
                       cow=cow, customer=customer, employee=employee)
    session.add(sale)
    session.commit()
    print(f"Sales record added successfully!")

# View Sales Records
def view_sales_records():
    sales = session.query(SalesRecord).all()
    for sale in sales:
        print(f"Date: {sale.sale_date}, Quantity: {sale.quantity_sold}L, Price: {sale.price}")
        print(f"Cow: {sale.cow.name}, Customer: {sale.customer.name}, Employee: {sale.employee.name}\n")