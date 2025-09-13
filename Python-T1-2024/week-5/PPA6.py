def mysterious(w):
    pass

def type_of_sequence(words):
    n = 0
    for w in words:
        n += int(mysterious(w))

    if n < 2:
        print('mildly mysterious')
    elif n < 5:
        print('moderately mysterious')
    else:
        print('mostly mysterious')
