n = int(input())

sol_found = False

for x in range(1, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1,n):
            equation = x**2 +y**2 == z**2
            if equation:
                sol_found = True
                print(f'{x},{y},{z}')

if not sol_found:
    print('NO SOLUTION')                