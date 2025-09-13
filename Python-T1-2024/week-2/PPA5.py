x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3 = float(input())

if x1 != x2:
    m = (y2 - y1) / (x2 - x1)   # m is the slope
    y3 = y1 + m * (x3 - x1)
    print(y3)

    if m == 0:
        print('Horizontal Line')
    elif m > 0:
        print('Positive Slope')
    else:
        print('Negative Slope')
else:
    print('Vertical Line')