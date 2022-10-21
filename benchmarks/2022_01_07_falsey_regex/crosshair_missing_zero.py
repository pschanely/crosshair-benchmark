import json
import re
from typing import Tuple

MISSING_ZERO = re.compile(
    r"""
\s*
(
    null
  | false
  | ""
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
        bool(MISSING_ZERO.fullmatch(s)),
    )
