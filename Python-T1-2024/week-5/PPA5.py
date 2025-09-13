# def first_three(L):
#     for i in L:
#         L.sort(i)
#         if i > 3:
#             return L 


def first_three(L):
    fmax = max(L)
    L.remove(fmax)

    smax = max(L)
    L.remove(smax)

    tmax = max(L)
    L.remove(tmax)

    return fmax, smax, tmax
