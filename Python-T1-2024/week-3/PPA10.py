n = int(input())

sum = 0

for i in range(2,n+1):
    is_prime = True
    # print(f'{i=}')
    for j in range(2, i):
        # print(f'{j=}')
        if i % j == 0:
            is_prime = False
    if is_prime:
        sum += i
print(sum)    