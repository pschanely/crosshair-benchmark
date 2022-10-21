import json
import re
from typing import Tuple

MISSING_NEGATIVE_ZERO = re.compile(
    r"""
\s*
(
    null
  | false
  | ""
  | 0 (\.0+)? ([eE] [\-\+]? [0-9]+)?
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
        bool(MISSING_NEGATIVE_ZERO.fullmatch(s)),
    )
