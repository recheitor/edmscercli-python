from datetime import datetime, timedelta
from time_off_request import TimeOffRequest
from utils import get_current_datetime

def add_time_off_request(connection, request: TimeOffRequest) -> None:
    """
    Adds a new time off request to the database, with various checks.

    Parameters
    ----------
    connection : sqlite3.Connection
        The connection to the SQLite database.
    request : TimeOffRequest
        The time off request object to be added.

    Raises
    ------
    ValueError
        If the request dates are invalid or if there is an overlapping request.
    """
    current_date = get_current_datetime()
    if request.start_date < current_date or request.end_date < current_date:
        raise ValueError("You can't select previous dates than today.")

    if request.end_date < request.start_date:
        raise ValueError("End date cannot be earlier than start date.")

    overlapping_requests = connection.execute('''
        SELECT tor.id, rc.name, tor.start_date, tor.end_date
        FROM time_off_requests tor
        JOIN request_categories rc ON tor.request_category_id = rc.id
        WHERE tor.employee_id = ?
        AND ((tor.start_date BETWEEN ? AND ?)
        OR (tor.end_date BETWEEN ? AND ?)
        OR (? BETWEEN tor.start_date AND tor.end_date)
        OR (? BETWEEN tor.start_date AND tor.end_date))
    ''', (str(request.employee_id), request.start_date.isoformat(), request.end_date.isoformat(),
          request.start_date.isoformat(), request.end_date.isoformat(),
          request.start_date.isoformat(), request.end_date.isoformat())).fetchall()

    for existing_request in overlapping_requests:
        if existing_request[1] == "Sick Leave" and request.request_category_id == 1:
            raise ValueError("Remote Work is not allowed to overlap with Sick Leave")

    if not overlapping_requests:
        with connection:
            connection.execute('''
                INSERT INTO time_off_requests (id, request_category_id, employee_id, start_date, end_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (str(request.id), request.request_category_id, str(request.employee_id),
                  request.start_date.isoformat(), request.end_date.isoformat()))
    else:
        previous_request = None
        for existing_request in overlapping_requests:
            if existing_request[1] == "Work Remotely":
                previous_request = existing_request
                break