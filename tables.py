def create_tables(connection) -> None:
    """
    Creates the necessary tables if they do not exist.

    Parameters
    ----------
    connection : sqlite3.Connection
        The connection to the SQLite database.
    """
    with connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS employees (
            employee_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            email TEXT NOT NULL,
            salary REAL NOT NULL,
            created_at TEXT NOT NULL,
            modified_at TEXT NOT NULL
        )''')
        connection.execute('''CREATE TABLE IF NOT EXISTS request_categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )''')
        connection.execute('''CREATE TABLE IF NOT EXISTS time_off_requests (
            id TEXT PRIMARY KEY,
            request_category_id INTEGER NOT NULL,
            employee_id TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            FOREIGN KEY (request_category_id) REFERENCES request_categories (id),
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
        )''')