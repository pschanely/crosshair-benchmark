from datetime import date, timedelta


def date_addition(base_date: date):
    """
    raises: OverflowError
    post: __return__ != date(2022, 10, 6)
    """
    return base_date + timedelta(days=0)
    # TODO: I'd like to get to this: return base_date + timedelta(days=8314)
