# def get_range(L):

    # max = []
    # min = []

    # for i in range(L):
    #     if i > max:
    #         max = i
    #     if i < min:
    #         min = i
    # return max - min

def maxi(L):
    maxi = L[0]
    for x in L:
        if x > maxi:
            maxi = x
    return maxi

def mini(L):
    mini = L[0]
    for y in  L:
        if y < mini:
            mini = y
    return mini

def get_range(L):
    return maxi - mini