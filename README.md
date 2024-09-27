# Dairy Farm Management System

Welcome to the **Dairy Farm Management System**! This Python project uses Object-Oriented Programming (OOP) and SQLAlchemy to manage the operations of a dairy farm, focusing on cows, employees, lactation records, customers, and sales.

#### By

This project is the property of Ian Dan K.

## Project Overview

The **Dairy Farm Management System** models a system that handles:

- Cow management (adding, viewing, and deleting cows)
- Employee management (adding, viewing, and deleting employees)
- Lactation records (tracking milk production for each cow)
- Customer management (adding and viewing customer information)
- Sales record management (handling sales of milk to customers)

### Relationships:

- A cow can have multiple lactation records.
- Sales records link cows, customers, and employees, tracking milk sales transactions.

## Features

- **Cow Management**: Create, view, and delete cow records, including their breed information.
- **Employee Management**: Manage employees, including adding, viewing, and deleting employee profiles.
- **Lactation Records**: Track milk production per cow, recording dates and quantities produced.
- **Customer Management**: Store customer details and view all registered customers.
- **Sales Records**: Generate sales records for transactions involving customers, cows, and employees. Track quantities sold and total sales price.
- **Data Display**: View all records (cows, employees, lactation records, customers, and sales) in a tabular format using the `rich` library for a better command-line interface experience.

## Further Explanations

- **add_cow**: Adds a new cow to the system, requiring a name and breed.
- **delete_cow**: Deletes a cow by ID after validation.
- **view_all_cows**: Displays all cows in the system in a tabular format.
  
- **add_employee**: Adds a new employee, requiring a name and position.
- **delete_employee**: Deletes an employee by ID after validation.
- **view_all_employees**: Displays all employees in a tabular format.

- **add_lactation_record**: Records milk production for a cow by inputting the quantity and date.
- **delete_lactation_record**: Deletes a lactation record by its ID.
- **view_all_lactation_records**: Displays all lactation records, showing details about the cow, date, and milk produced.

- **add_customer**: Adds a customer with their contact information.
- **view_all_customers**: Displays all customers in a tabular format.

- **generate_sales_record**: Records a milk sale, linking a cow, customer, employee, and transaction details.
- **view_sales_records**: Displays all sales transactions in a detailed table.

- **menu**: Main loop for the CLI, handling user inputs and invoking corresponding methods.

## Setup/Installation Requirements

- Linux or WSL for Windows users
- Visual Studio Code installed
- GitHub account
- Python 3.x
- SQLite Database

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/IanDanCheruiyot/project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd dairy-farm-management
   ```

3. Open the project in Visual Studio Code:
   ```bash
   $ code .
   ```

## Running the Application

1. Ensure Python 3.x is installed on your machine.

2. Set Up the Virtual Environment: This project uses `pipenv` for managing dependencies:

   ```bash
   $ pipenv install
   $ pipenv shell
   ```

3. Run database migrations with Alembic:

   ```bash
   $ alembic upgrade head
   ```

4. To run the application, execute the main script:
   ```bash
   $ python3 app/main.py
   ```

## Technologies Used

This project is built with:

- Python 3.x
- SQLAlchemy ORM
- SQLite Database
- Alembic for database migrations
- `rich` for enhanced CLI output

## Support and Contact Details

For any issues, feel free to email me at ian.cheruiyot1@student.moringa.com.

## License

This project is licensed under the MIT License.

- See the [LICENSE](./LICENSE) file for details.
