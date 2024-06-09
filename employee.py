from typing import Final
from uuid import UUID, uuid4
from datetime import datetime

class Employee:
    def __init__(self, employee_id: Final[UUID], name: Final[str], position: Final[str],
                 email: Final[str], salary: Final[float], created_at: Final[datetime], modified_at: Final[datetime]) -> None:
        self.employee_id: Final[UUID] = employee_id
        self.name: Final[str] = name
        self.position: Final[str] = position
        self.email: Final[str] = email
        self.salary: Final[float] = salary
        self.created_at: Final[datetime] = created_at
        self.modified_at: Final[datetime] = modified_at

    def __str__(self) -> str:
        return (f"Employee [ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, "
                f"Email: {self.email}, Salary: {self.salary}, Created At: {self.created_at}, "
                f"Modified At: {self.modified_at}]")
