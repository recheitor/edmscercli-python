from uuid import uuid4
from employee import Employee
from request_category import RequestCategory
from utils import get_current_datetime

def setup_database(db):
    # Add request categories
    work_remotely = RequestCategory(id=1, name="Work Remotely")
    annual_leave = RequestCategory(id=2, name="Annual Leave")
    sick_leave = RequestCategory(id=3, name="Sick Leave")
    db.add_request_category(work_remotely)
    db.add_request_category(annual_leave)
    db.add_request_category(sick_leave)

    # Add employees
    emp1 = Employee(
        employee_id=uuid4(),
        name="Alex Reche",
        position="Dev",
        email="alex.re@cercli.com",
        salary=60000.0,
        created_at=get_current_datetime(),
        modified_at=get_current_datetime()
    )

    emp2 = Employee(
        employee_id=uuid4(),
        name="David Reche",
        position="Sup",
        email="david.re@cercli.com",
        salary=80000.0,
        created_at=get_current_datetime(),
        modified_at=get_current_datetime()
    )

    db.add_employee(emp1)
    db.add_employee(emp2)

    return emp1, emp2, work_remotely, annual_leave, sick_leave