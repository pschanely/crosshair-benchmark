def f(d: dict) -> dict:
    """
    pre: d["age1"] < 100 < d["age2"]
    post: __return__ != {"age1": 100, "age2": 100}
    """
    d["age1"] += 1
    d["age2"] -= 1
    return d
