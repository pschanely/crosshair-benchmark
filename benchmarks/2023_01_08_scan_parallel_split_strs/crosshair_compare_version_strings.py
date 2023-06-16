#def compare_version_strings(version1: str, version2: str) -> int:
def compare_version_strings(version1, version2):
    """
    pre: isinstance(version1, str) and isinstance(version2, str)
    pre: len(version1) == 3 and len(version2) == 3
    raises: ValueError
    post: __return__ != 0
    """
    v1 = version1.split(".")
    v2 = version2.split(".")
    for i in range(max(len(v1), len(v2))):
        v1i = int(v1[i]) if i < len(v1) else 0
        v2i = int(v2[i]) if i < len(v2) else 0
        if v1i > v2i:
            return 1
        elif v1i < v2i:
            return -1
    return 0
