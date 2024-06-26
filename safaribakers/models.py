import sqlite3

class EmployeeManagement:
    def __init__(self, db_name='employee_management.db'):
        try:
            self.conn = sqlite3.connect(db_name)
            self.create_tables()
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    # Create tables if they don't exist
    def create_tables(self):
        c = self.conn.cursor()
        # Create employees table
        c.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        position TEXT,
                        salary REAL,
                        department_id INTEGER,
                        FOREIGN KEY (department_id) REFERENCES departments(id)
                     )''')
        # Create departments table
        c.execute('''CREATE TABLE IF NOT EXISTS departments (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE
                     )''')
        # Create shifts table
        c.execute('''CREATE TABLE IF NOT EXISTS shifts (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        employee_id INTEGER,
                        FOREIGN KEY (employee_id) REFERENCES employees(id)
                     )''')
        self.conn.commit()

    # Add an employee to the database
    def add_employee(self, name, position, salary, department_name):
        try:
            # Get the department ID by name
            department_id = self.get_department_id_by_name(department_name)
            if department_id is None:
                print(f"Department '{department_name}' does not exist. Please add it first.")
                return
            # Insert employee data into the database
            c = self.conn.cursor()
            c.execute('''INSERT INTO employees (name, position, salary, department_id)
                         VALUES (?, ?, ?, ?)''', (name, position, salary, department_id))
            self.conn.commit()
            print("Employee added successfully.")
        except sqlite3.IntegrityError as e:
            print("Error:", e)

    # View all employees
    def view_employees(self):
        c = self.conn.cursor()
        c.execute('''SELECT e.id, e.name, e.position, e.salary, d.name AS department_name
                     FROM employees e
                     LEFT JOIN departments d ON e.department_id = d.id''')
        employees = c.fetchall()
        if not employees:
            print("No employees found.")
            return
        print("Employee ID | Name | Position | Salary | Department")
        for employee in employees:
            print(f"{employee[0]} | {employee[1]} | {employee[2]} | {employee[3]} | {employee[4]}")

    # Add a department to the database
    def add_department(self, name):
        try:
            # Insert department data into the database
            c = self.conn.cursor()
            c.execute('''INSERT INTO departments (name) VALUES (?)''', (name,))
            self.conn.commit()
            print("Department added successfully.")
        except sqlite3.IntegrityError as e:
            print("Error:", e)

    # List all departments
    def list_departments(self):
        c = self.conn.cursor()
        c.execute('''SELECT * FROM departments''')
        departments = c.fetchall()
        if not departments:
            print("No departments found.")
            return
        print("Department ID | Name")
        for department in departments:
            print(f"{department[0]} | {department[1]}")

    # Delete an employee by ID
    def delete_employee(self, employee_id):
        try:
            # Delete employee from the database
            c = self.conn.cursor()
            c.execute('''DELETE FROM employees WHERE id = ?''', (employee_id,))
            self.conn.commit()
            print("Employee deleted successfully.")
        except sqlite3.IntegrityError as e:
            print("Error:", e)

    # Display employees by department
    def display_employees_by_department(self, department_name):
        department_id = self.get_department_id_by_name(department_name)
        if department_id is None:
            print(f"Department '{department_name}' does not exist.")
            return
        c = self.conn.cursor()
        c.execute('''SELECT * FROM employees WHERE department_id = ?''', (department_id,))
        employees = c.fetchall()
        if not employees:
            print(f"No employees found in department '{department_name}'.")
            return
        print(f"Employees in department '{department_name}':")
        for employee in employees:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}")

    # Add a shift for an employee
    def add_shift(self, date, employee_id):
        try:
            # Insert shift data into the database
            c = self.conn.cursor()
            c.execute('''INSERT INTO shifts (date, employee_id)
                         VALUES (?, ?)''', (date, employee_id))
            self.conn.commit()
            print("Shift added successfully.")
        except sqlite3.IntegrityError as e:
            print("Error:", e)

    # View shifts for an employee by ID
    def view_shifts(self, employee_id):
        c = self.conn.cursor()
        c.execute('''SELECT * FROM shifts WHERE employee_id = ?''', (employee_id,))
        shifts = c.fetchall()
        if not shifts:
            print("No shifts found for the employee.")
            return
        print(f"Shifts for Employee ID {employee_id}:")
        for shift in shifts:
            print(f"ID: {shift[0]}, Date: {shift[1]}")

    # Get department ID by name
    def get_department_id_by_name(self, name):
        c = self.conn.cursor()
        c.execute('''SELECT id FROM departments WHERE name = ?''', (name,))
        result = c.fetchone()
        if result:
            return result[0]
        else:
            return None
