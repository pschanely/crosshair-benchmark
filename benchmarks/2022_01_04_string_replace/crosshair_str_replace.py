def find_in_replaced_string(n: str) -> str:
    """
    post: not('py' in __return__)
    """
    if "py" in n:
        return ""
    n = n.replace("./", "")
    return n
