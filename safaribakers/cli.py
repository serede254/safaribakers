import click
from models import EmployeeManagement

@click.group()
def cli():
    """SAFARI BAKERS EMPLOYEE MANAGEMENT SYSTEM"""
    pass

@cli.command()
@click.option('--name', prompt='Employee name', help='Enter the name of the employee')
@click.option('--position', prompt='Employee position', help='Enter the position of the employee')
@click.option('--salary', prompt='Employee salary', help='Enter the salary of the employee')
@click.option('--department-name', prompt='Department name', help='Enter the name of the department')
def add_employee(name, position, salary, department_name):
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.add_employee(name, position, salary, department_name)

@cli.command()
def view_employees():
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.view_employees()

@cli.command()
@click.option('--name', prompt='Department name', help='Enter the name of the department')
def add_department(name):
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.add_department(name)

@cli.command()
def list_departments():
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.list_departments()

@cli.command()
@click.argument('employee_id', type=int)
def delete_employee(employee_id):
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.delete_employee(employee_id)

@cli.command()
@click.argument('department_name')
def display_employees_by_department(department_name):
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.display_employees_by_department(department_name)

@cli.command()
@click.option('--date', prompt='Shift date', help='Enter the shift date (YYYY-MM-DD)')
@click.option('--employee-id', prompt='Employee ID', help='Enter the employee ID for the shift')
def add_shift(date, employee_id):
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.add_shift(date, employee_id)

@cli.command()
@click.argument('employee_id', type=int)
def view_shifts(employee_id):
    
    emp_mgmt = EmployeeManagement()
    emp_mgmt.view_shifts(employee_id)

if __name__ == '__main__':
    cli()
