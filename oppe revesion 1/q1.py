# swapping 

def minmax(a, b):

    for i in a:
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
    return max(a)*max(b)
    print()