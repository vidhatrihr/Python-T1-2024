num_1 = int(input())
num_2 = int(input())

coprime = True

for i in range(num_1):
    if num_1 % i == 0 and num_2 % i == 0:
        # print(i)
        coprime = False
        break 
if coprime:
    print('Coprime')
else:
    print('Not Coprime')