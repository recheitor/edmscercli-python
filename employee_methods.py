from typing import List, Optional
from uuid import UUID
from datetime import datetime
from employee import Employee
from utils import is_valid_email

def add_employee(connection, employee: Employee) -> None:
    """
    Adds a new employee to the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The connection to the SQLite database.
    employee : Employee
        The employee object to be added.

    Raises
    ------
    ValueError
        If the email format is invalid.
    """
    if not is_valid_email(employee.email):
        raise ValueError("Invalid email format")
    with connection:
        connection.execute('''
            INSERT INTO employees (employee_id, name, position, email, salary, created_at, modified_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (str(employee.employee_id), employee.name, employee.position, employee.email,
              employee.salary, employee.created_at.isoformat(), employee.modified_at.isoformat()))

def update_employee(connection, employee: Employee) -> None:
    """
    Updates an existing employee's details in the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The connection to the SQLite database.
    employee : Employee
        The employee object with updated details.
    """
    with connection:
        connection.execute('''
            UPDATE employees
            SET name = ?, position = ?, email = ?, salary = ?, created_at = ?, modified_at = ?
            WHERE employee_id = ?
        ''', (employee.name, employee.position, employee.email, employee.salary,
              employee.created_at.isoformat(), employee.modified_at.isoformat(), str(employee.employee_id)))

def get_employee(connection, employee_id: UUID) -> Optional[Employee]:
    """
    Retrieves an employee by their ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        The connection to the SQLite database.
    employee_id : UUID
        The ID of the employee to be retrieved.

    Returns
    -------
    Optional[Employee]
        The employee object if found, otherwise None.
    """
    employee_row = connection.execute('''
        SELECT employee_id, name, position, email, salary, created_at, modified_at
        FROM employees
        WHERE employee_id = ?
    ''', (str(employee_id),)).fetchone()

    if employee_row:
        return Employee(
            employee_id=UUID(employee_row[0]),
            name=employee_row[1],
            position=employee_row[2],
            email=employee_row[3],
            salary=employee_row[4],
            created_at=datetime.fromisoformat(employee_row[5]),
            modified_at=datetime.fromisoformat(employee_row[6])
        )
    return None

def get_all(connection) -> List[Employee]:
    """
    Retrieves all employees from the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The connection to the SQLite database.

    Returns
    -------
    List[Employee]
        A list of all employee objects.
    """
    employees = []
    employee_rows = connection.execute('''
        SELECT employee_id, name, position, email, salary, created_at, modified_at
        FROM employees
    ''').fetchall()

    for row in employee_rows:
        employees.append(Employee(
            employee_id=UUID(row[0]),
            name=row[1],
            position=row[2],
            email=row[3],
            salary=row[4],
            created_at=datetime.fromisoformat(row[5]),
            modified_at=datetime.fromisoformat(row[6])
        ))
    return employees