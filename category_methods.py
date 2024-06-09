from request_category import RequestCategory

def add_request_category(connection, category: RequestCategory) -> None:
    """
    Adds a new request category to the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The connection to the SQLite database.
    category : RequestCategory
        The request category object to be added.
    """
    with connection:
        connection.execute('''
            INSERT INTO request_categories (id, name)
            VALUES (?, ?)
        ''', (category.id, category.name))