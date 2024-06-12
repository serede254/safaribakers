import click
from models import EmployeeManagement

@click.group()
def cli():
    """SAFARI BAKERS EMPLOYEE MANAGEMENT SYSTEM"""
    pass

# Command to add an employee
@cli.command()
@click.option('--name', prompt='Employee name', help='Enter the name of the employee')
@click.option('--position', prompt='Employee position', help='Enter the position of the employee')
@click.option('--salary', prompt='Employee salary', help='Enter the salary of the employee')
@click.option('--department-name', prompt='Department name', help='Enter the name of the department')
def add_employee(name, position, salary, department_name):
    """Add a new employee"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.add_employee(name, position, salary, department_name)

# Command to view all employees
@cli.command()
def view_employees():
    """View all employees"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.view_employees()

# Command to add a department
@cli.command()
@click.option('--name', prompt='Department name', help='Enter the name of the department')
def add_department(name):
    """Add a new department"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.add_department(name)

# Command to list all departments
@cli.command()
def list_departments():
    """List all departments"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.list_departments()

# Command to delete an employee
@cli.command()
@click.argument('employee_id', type=int)
def delete_employee(employee_id):
    """Delete an employee by ID"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.delete_employee(employee_id)

# Command to display employees by department
@cli.command()
@click.argument('department_name')
def display_employees_by_department(department_name):
    """Display employees in a department by name"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.display_employees_by_department(department_name)

# Command to add a shift
@cli.command()
@click.option('--date', prompt='Shift date(YYYY-MM-DD)', help='Enter the shift date (YYYY-MM-DD)')
@click.option('--employee-id', prompt='Employee ID', help='Enter the employee ID for the shift')
def add_shift(date, employee_id):
    """Add a shift for an employee"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.add_shift(date, employee_id)

# Command to view shifts for an employee
@cli.command()
@click.argument('employee_id', type=int)
def view_shifts(employee_id):
    """View shifts for an employee by ID"""
    emp_mgmt = EmployeeManagement()
    emp_mgmt.view_shifts(employee_id)

if __name__ == '__main__':
    cli()
