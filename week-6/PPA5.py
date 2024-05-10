def dict_to_list(D):
    my_list = []
    for key in D:
        my_list.append((key, D[key]))
        return my_list
    