import re
import json
from typing import Tuple

MISSING_MULTIDECIMAL_FLOAT_ZERO = re.compile(r'''
\s*
(
    null
  | false
  | ""
  | \-? 0 (\.0)? ([eE] [\-\+]? [0-9]+)?
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
        bool(MISSING_MULTIDECIMAL_FLOAT_ZERO.fullmatch(s)),
    )

