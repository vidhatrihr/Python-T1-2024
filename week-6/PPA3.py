def is_key(D, key):
    return key in D

def value(D, key):
    if not is_key(D, key):
        return None
    return D[key]
