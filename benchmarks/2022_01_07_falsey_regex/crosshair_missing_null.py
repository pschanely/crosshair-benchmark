import json
import re
from typing import Tuple

MISSING_NULL = re.compile(
    r"""
\s*
(
    false
  | ""
  | \-? 0 (\.0+)? ([eE] [\-\+]? [0-9]+)?
  | \{ \s* \}
  | \[ \s* \]
)
\s*
""",
    re.VERBOSE,
)


def test_regex_is_falsey(s: str) -> Tuple[bool, bool]:
    """
    post: _[0] != _[1]
    raises: json.JSONDecodeError
    """
    return (
        bool(json.loads(s)),
        bool(MISSING_NULL.fullmatch(s)),
    )
