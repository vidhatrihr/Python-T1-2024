e1 = int(input())
e2 = int(input())
e3 = int(input())
e4 = int(input())
e5 = int(input())

sum1 = e1 + e2
sum2 = e2 + e3
sum3 = e3 + e4
sum4 = e4 + e5
sum5 = e5 + e1

if sum1 % 2 == 0 and sum2 % 2 == 0 and sum3 % 2 == 0 and sum4 % 2 == 0 and sum5 % 2 == 0:
    print('YES')
else:
    print('NO')