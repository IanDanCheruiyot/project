#import re
from models import Base
from rich import print
from rich.table import Table
from rich.console import Console
from models import session, Cow, LactationRecord, Employee, Customer, SalesRecord
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///dairy_farm.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class DairyFarm:
    def __init__(self):
        self.session = session
        self.console = Console()

    # COW MANAGEMENT

    def add_cow(self):
        name = input("Enter cow's name: ").strip()
        breed = input("Enter cow's breed: ").strip()

        if not name or not breed:
            print("Name and breed are required.")
            return

        cow = Cow(name=name, breed=breed)
        self.session.add(cow)
        self.session.commit()
        print(f"Cow '{name}' added successfully!")

    def delete_cow(self):
        cow_id = input("Enter cow ID to delete: ")
        try:
            cow_id = int(cow_id)
            cow = self.session.query(Cow).get(cow_id)
            if cow:
                self.session.delete(cow)
                self.session.commit()
                print(f"Cow with ID {cow_id} deleted successfully!")
            else:
                print(f"Cow with ID {cow_id} not found!")
        except ValueError:
            print("Invalid ID. Please enter a number.")

    def view_all_cows(self):
        cows = self.session.query(Cow).all()
        if cows:
            table = Table(title="Cows")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Breed", style="green")
            for cow in cows:
                table.add_row(str(cow.id), cow.name, cow.breed)
            self.console.print(table)
        else:
            print("No cows found!")

    # EMPLOYEE MANAGEMENT

    def add_employee(self):
        name = input("Enter employee name: ").strip()
        position = input("Enter employee position: ").strip()

        if not name or not position:
            print("Name and position are required.")
            return

        employee = Employee(name=name, position=position)
        self.session.add(employee)
        self.session.commit()
        print(f"Employee '{name}' added successfully!")

    def delete_employee(self):
        employee_id = input("Enter employee ID to delete: ")
        try:
            employee_id = int(employee_id)
            employee = self.session.query(Employee).get(employee_id)
            if employee:
                self.session.delete(employee)
                self.session.commit()
                print(f"Employee with ID {employee_id} deleted successfully!")
            else:
                print(f"Employee with ID {employee_id} not found!")
        except ValueError:
            print("Invalid ID. Please enter a number.")

    def view_all_employees(self):
        employees = self.session.query(Employee).all()
        if employees:
            table = Table(title="Employees")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Position", style="green")
            for employee in employees:
                table.add_row(str(employee.id), employee.name, employee.position)
            self.console.print(table)
        else:
            print("No employees found!")

    # LACTATION RECORD MANAGEMENT

    def add_lactation_record(self):
        cow_id = input("Enter cow ID: ")
        date = input("Enter record date (YYYY-MM-DD): ").strip()
        milk_produced = input("Enter milk produced (liters): ")

        try:
            cow_id = int(cow_id)
            milk_produced = float(milk_produced)

            record_date = datetime.strptime(date, "%Y-%m-%d").date()

            cow = self.session.query(Cow).get(cow_id)
            if not cow:
                print(f"Cow with ID {cow_id} not found!")
                return

            lactation_record = LactationRecord(date=record_date, milk_produced=milk_produced, cow=cow)
            self.session.add(lactation_record)
            self.session.commit()
            print(f"Lactation record for cow '{cow.name}' added successfully!")
        except ValueError:
            print("Invalid input. Ensure you enter a valid cow ID and milk quantity.")

    def delete_lactation_record(self):
        record_id = input("Enter lactation record ID to delete: ")
        try:
            record_id = int(record_id)
            record = self.session.query(LactationRecord).get(record_id)
            if record:
                self.session.delete(record)
                self.session.commit()
                print(f"Lactation record with ID {record_id} deleted successfully!")
            else:
                print(f"Lactation record with ID {record_id} not found!")
        except ValueError:
            print("Invalid ID. Please enter a number.")

    def view_all_lactation_records(self):
        records = self.session.query(LactationRecord).all()
        if records:
            table = Table(title="Lactation Records")
            table.add_column("ID", style="cyan")
            table.add_column("Date", style="magenta")
            table.add_column("Milk Produced (L)", style="green")
            table.add_column("Cow", style="yellow")
            for record in records:
                table.add_row(str(record.id), record.date, str(record.milk_produced), record.cow.name)
            self.console.print(table)
        else:
            print("No lactation records found!")

    # CUSTOMER MANAGEMENT

    def add_customer(self):
        name = input("Enter customer name: ").strip()
        contact_info = input("Enter customer contact info: ").strip()

        if not name:
            print("Customer name is required.")
            return

        customer = Customer(name=name, contact_info=contact_info)
        self.session.add(customer)
        self.session.commit()
        print(f"Customer '{name}' added successfully!")

    def delete_customer(self):
        customer_id = input("Enter customer ID to delete: ")
        try:
            customer_id = int(customer_id)
            customer = self.session.query(Customer).get(customer_id)
            if customer:
                self.session.delete(customer)
                self.session.commit()
                print(f"Customer with ID {customer_id} deleted successfully!")
            else:
                print(f"Customer with ID {customer_id} not found!")
        except ValueError:
            print("Invalid ID. Please enter a number.")

    def view_all_customers(self):
        customers = self.session.query(Customer).all()
        if customers:
            table = Table(title="Customers")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Contact Info", style="green")
            for customer in customers:
                table.add_row(str(customer.id), customer.name, customer.contact_info)
            self.console.print(table)
        else:
            print("No customers found!")

    # SALES RECORD MANAGEMENT

    def generate_sales_record(self):
        cow_id = input("Enter cow ID: ")
        customer_id = input("Enter customer ID: ")
        employee_id = input("Enter employee ID: ")
        sale_date = input("Enter sale date (YYYY-MM-DD): ")
        quantity_sold = input("Enter milk quantity sold (in liters): ")
        price = input("Enter sale price (total): ")

        try:
            cow_id = int(cow_id)
            customer_id = int(customer_id)
            employee_id = int(employee_id)
            quantity_sold = float(quantity_sold)
            price = float(price)

            cow = self.session.query(Cow).get(cow_id)
            customer = self.session.query(Customer).get(customer_id)
            employee = self.session.query(Employee).get(employee_id)

            if not cow or not customer or not employee:
                print("Invalid cow, customer, or employee ID.")
                return

            sale = SalesRecord(sale_date=sale_date, quantity_sold=quantity_sold, price=price,
                               cow=cow, customer=customer, employee=employee)
            self.session.add(sale)
            self.session.commit()
            print("Sales record added successfully!")
        except ValueError:
            print("Invalid input. Ensure you enter valid IDs and numeric values.")

    def view_sales_records(self):
        sales = self.session.query(SalesRecord).all()
        if sales:
            table = Table(title="Sales Records")
            table.add_column("Date", style="cyan")
            table.add_column("Quantity (L)", style="magenta")
            table.add_column("Price", style="green")
            table.add_column("Cow", style="yellow")
            table.add_column("Customer", style="yellow")
            table.add_column("Employee", style="yellow")
            for sale in sales:
                table.add_row(sale.sale_date, str(sale.quantity_sold), f"${sale.price:.2f}",
                              sale.cow.name, sale.customer.name, sale.employee.name)
            self.console.print(table)
        else:
            print("No sales records found!")

    # MAIN CLI MENU

    def menu(self):
        while True:
            print("\n--- Dairy Farm Management ---")
            print("1. Add Cow")
            print("2. View All Cows")
            print("3. Delete Cow")
            print("4. Add Employee")
            print("5. View All Employees")
            print("6. Delete Employee")
            print("7. Add Lactation Record")
            print("8. View All Lactation Records")
            print("9. Delete Lactation Record")
            print("10. Add Customer")
            print("11. Generate Sales Record")
            print("12. View Sales Records")
            print("0. Exit")
            
            choice = input("Choose an option: ").strip()
            
            if choice == '1':
                self.add_cow()
            elif choice == '2':
                self.view_all_cows()
            elif choice == '3':
                self.delete_cow()
            elif choice == '4':
                self.add_employee()
            elif choice == '5':
                self.view_all_employees()
            elif choice == '6':
                self.delete_employee()
            elif choice == '7':
                self.add_lactation_record()
            elif choice == '8':
                self.view_all_lactation_records()
            elif choice == '9':
                self.delete_lactation_record()
            elif choice == '10':
                self.add_customer()
            elif choice == '11':
                self.generate_sales_record()
            elif choice == '12':
                self.view_sales_records()
            elif choice == '0':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Try again.")

def main():
    dairy_farm = DairyFarm()
    dairy_farm.menu()   
if __name__ == "__main__":
    main()             