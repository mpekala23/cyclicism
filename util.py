from datetime import datetime


def month_to_str(date: datetime):
    """
    Converts a datetime object to a string for metadata db
    """
    return date.strftime("%m-%Y")


def str_to_month(s: str):
    """
    Converts a string representing a month into a datetime
    """
    month, year = s.split("-")
    return datetime(year=int(year), month=int(month), day=1)
