def is_empty(L):
    if len(L) == 0:
        return True
    else:
        return False
    
def first(L):
    return L[0] if len(L) != 0 else 'None'

def last(L):
    return L[-1] if len(L) != 0 else 'None'

def inti(L):
    return L[:-1] if len(L) != 0 else 'None'

def rest(L):
    return L[1:] if len(L) != 0 else 'None'
