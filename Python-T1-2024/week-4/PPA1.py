# n = int(input())
# next_no = 0

# for i in range(n):
#     if i > 0:
#         print(f'[{i-(i-1)},{i}]')
# concept of concatination or append. for adding use loop

n = int(input())

L = []

for i in range(1,n+1):
    L.append(i)
# print(L)

# or

L = []
for i in range(1, n+1):
    L= L + [i]
# print(L)

n = int(input())
L = [i for i in range(n+1) if i > 0]
print(L)