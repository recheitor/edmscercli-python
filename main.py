from uuid import uuid4
from datetime import datetime, timedelta
from employee import Employee
from database import EmployeeDatabase
from utils import get_current_datetime
from time_off_request import TimeOffRequest
from setup_data import setup_database

def main() -> None:
    db = EmployeeDatabase()

    emp1, emp2, work_remotely, annual_leave, sick_leave = setup_database(db)

    print("All employees:")
    print(db)

    print("\nRetrieve employee by ID:")
    emp = db.get_employee(emp1.employee_id)
    if emp:
        print(emp)
    else:
        print("Employee not found")

    # Test updating an employee
    print("\nUpdating employee salary:")
    updated_emp1 = Employee(
        employee_id=emp1.employee_id,
        name=emp1.name,
        position=emp1.position,
        email=emp1.email,
        salary=65000.0,  # Updated salary
        created_at=emp1.created_at,
        modified_at=get_current_datetime()
    )
    db.update_employee(updated_emp1)
    print(db.get_employee(emp1.employee_id))

    # Test invalid email
    try:
        emp_invalid_email = Employee(
            employee_id=uuid4(),
            name="Invalid Email",
            position="Tester",
            email="invalid-email",  # Invalid email
            salary=50000.0,
            created_at=get_current_datetime(),
            modified_at=get_current_datetime()
        )
        db.add_employee(emp_invalid_email)
    except ValueError as e:
        print(f"Error: {e}")

    # Test time off requests
    current_date = get_current_datetime()

    # Valid request
    time_off1 = TimeOffRequest(
        id=uuid4(),
        request_category_id=work_remotely.id,
        employee_id=emp1.employee_id,
        start_date=current_date + timedelta(days=1),
        end_date=current_date + timedelta(days=4)
    )

    # Overlapping request from Work remotely and Annual leave category
    time_off2 = TimeOffRequest(
        id=uuid4(),
        request_category_id=annual_leave.id,
        employee_id=emp1.employee_id,
        start_date=current_date + timedelta(days=3),
        end_date=current_date + timedelta(days=6)
    )

    # Request in the past
    time_off_past = TimeOffRequest(
        id=uuid4(),
        request_category_id=annual_leave.id,
        employee_id=emp1.employee_id,
        start_date=current_date - timedelta(days=5),
        end_date=current_date - timedelta(days=3)
    )

    # End date before start date
    time_off_invalid_dates = TimeOffRequest(
        id=uuid4(),
        request_category_id=annual_leave.id,
        employee_id=emp1.employee_id,
        start_date=current_date + timedelta(days=5),
        end_date=current_date + timedelta(days=4)
    )

    # Overlapping request with sick leave and remote work
    time_off3 = TimeOffRequest(
        id=uuid4(),
        request_category_id=sick_leave.id,
        employee_id=emp1.employee_id,
        start_date=current_date + timedelta(days=7),
        end_date=current_date + timedelta(days=10)
    )

    time_off4 = TimeOffRequest(
        id=uuid4(),
        request_category_id=work_remotely.id,
        employee_id=emp1.employee_id,
        start_date=current_date + timedelta(days=8),
        end_date=current_date + timedelta(days=11)
    )

    try:
        db.add_time_off_request(time_off1)
        print("Time off request 1 added Remote Work successfully")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        db.add_time_off_request(time_off2)
        print("Time off request 2 added Annual Leave added successfully")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        db.add_time_off_request(time_off_past)
        print("Time off request in the past added successfully")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        db.add_time_off_request(time_off_invalid_dates)
        print("Time off request with invalid dates added successfully")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        db.add_time_off_request(time_off3)
        print("Time off request 3 (sick leave) added successfully")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        db.add_time_off_request(time_off4)
        print("Time off request 4 (remote work overlapping with sick leave) added successfully")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()