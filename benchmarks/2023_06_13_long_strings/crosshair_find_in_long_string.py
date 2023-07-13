def f(param: str) -> str:
    '''
    pre: "sx250ab" in param
    post: "sx250ab" not in __return__
    '''
    z = 'sx250aa'*30 + param + 'y'
    return z
