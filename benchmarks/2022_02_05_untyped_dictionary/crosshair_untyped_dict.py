def f(d: dict) -> dict:
    """
    pre: d["age"] < 100
    post: __return__["age"] < 100
    """
    d["age"] += 1
    return d
