import re
import json
from typing import Tuple

EXP_IN_UPPER_OR_LOWER_CASE = re.compile(r'''
\s*
(
    null
  | false
  | ""
  | \-? 0 (\.0+)? (e [\-\+]? [0-9]+)?
  | \{ \s* \}
  | \[ \s* \]
)
\s*
''', re.VERBOSE)

def test_regex_is_falsey(s: str) -> Tuple[bool, bool]:
    """
    post: _[0] != _[1]
    raises: json.JSONDecodeError
    """
    return (
        bool(json.loads(s)),
        bool(EXP_IN_UPPER_OR_LOWER_CASE.fullmatch(s)),
    )

