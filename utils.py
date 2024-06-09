from datetime import datetime, timedelta
import re

def get_current_datetime() -> datetime:
    server_offset = timedelta(hours=3)  # timezone difference
    return datetime.utcnow() + server_offset

def is_valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
