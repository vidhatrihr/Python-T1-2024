t = int(input())

if t < 0:
    print('Invalid') 
elif t <= 5:
    print('Night')
elif t <= 11:
    print('Morning')
elif t <= 17:
    print('Afternoon')
elif t <= 23:
    print('evening')
else:
    print('Invalid')