def dict_to_list(D):
    my_list = []
    for key in D:
        my_list.append((key, D[key]))
        return my_list
    
def list_to_dict(L):
    my_dict = {}
    for item in L:
        my_dict[item[0]] = item[1]
    return my_dict

    #  or using method

def dict_to_list(D):
    return list.list(D.items())



def list_to_dict(L):
    return{
        item[0]: item[1] for item in L
    }

