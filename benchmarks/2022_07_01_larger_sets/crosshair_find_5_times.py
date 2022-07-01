from typing import Set

def switch_is_on(t: int):
  return 5 <= t <= 17

def _check_time_periods(times: Set[int]):
  """
  pre: len(times) == 5
  post: __return__ != {True}
  """
  return set(map(switch_is_on, times))
