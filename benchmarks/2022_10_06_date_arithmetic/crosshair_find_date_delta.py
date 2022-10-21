from datetime import date, timedelta


def date_addition(delta: timedelta):
    """
    raises: OverflowError
    post: __return__ != date(2022, 10, 6)
    """
    return date(2000, 1, 1) + delta
