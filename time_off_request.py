from uuid import UUID
from datetime import datetime
from typing import Final

class TimeOffRequest:
    id: Final[UUID]
    request_category_id: Final[int]
    employee_id: Final[UUID]
    start_date: Final[datetime]
    end_date: Final[datetime]

    def __init__(self, id: UUID, request_category_id: int, employee_id: UUID, start_date: datetime, end_date: datetime) -> None:
        self.id = id
        self.request_category_id = request_category_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self) -> str:
        return (f"TimeOffRequest [ID: {self.id}, Request Category ID: {self.request_category_id}, "
                f"Employee ID: {self.employee_id}, Start Date: {self.start_date}, End Date: {self.end_date}]")
