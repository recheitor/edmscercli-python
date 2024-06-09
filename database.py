import sqlite3
from typing import List, Optional
from uuid import UUID
from datetime import datetime, timedelta
from employee import Employee
from request_category import RequestCategory
from time_off_request import TimeOffRequest
from utils import get_current_datetime, is_valid_email
from tables import create_tables
from employee_methods import add_employee, update_employee, get_employee, get_all
from category_methods import add_request_category
from time_off_methods import add_time_off_request

class EmployeeDatabase:
    """
    A class to represent the employee database.
    """

    def __init__(self, db_name: str = "employees.db") -> None:
        """
        Initializes the database connection and creates tables.
        """
        self.connection = sqlite3.connect(db_name)
        create_tables(self.connection)

    def add_employee(self, employee: Employee) -> None:
        add_employee(self.connection, employee)

    def update_employee(self, employee: Employee) -> None:
        update_employee(self.connection, employee)

    def get_employee(self, employee_id: UUID) -> Optional[Employee]:
        return get_employee(self.connection, employee_id)

    def get_all(self) -> List[Employee]:
        return get_all(self.connection)

    def add_request_category(self, category: RequestCategory) -> None:
        add_request_category(self.connection, category)

    def add_time_off_request(self, request: TimeOffRequest) -> None:
        add_time_off_request(self.connection, request)

    def __str__(self) -> str:
        employees = self.get_all()
        return '\n'.join([str(emp) for emp in employees])