
from typing import Dict, List, Union, Tuple, Set, Callable

AlowedColumns = Union[List[float], List[int], List[str]]
DfSimbolicInternal = Dict[str, AlowedColumns]


def shape(df: DfSimbolicInternal) -> Tuple[int, int]:
    return (len(df), len(next(iter(df.values()))))


def valid_dataframe(df: DfSimbolicInternal) -> bool:
    n_cols, n_rows = shape(df)
    return n_cols > 0 and n_rows > 0 and all(len(v) == n_rows for v in df.values())


def maybe_returns_true(k: DfSimbolicInternal, p: DfSimbolicInternal) -> bool:
    """
    pre: valid_dataframe(k)
    pre: "a" in k and "b" in k
    post: _
    """
    return False
