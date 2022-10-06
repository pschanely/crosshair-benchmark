from datetime import datetime, timedelta

def datetime_addition(delta: timedelta):
  """
  raises: OverflowError
  post: __return__ != datetime(2022, 10, 6, 13, 15, 59)
  """
  return datetime(2000, 1, 1, 11, 45, 00) + delta
