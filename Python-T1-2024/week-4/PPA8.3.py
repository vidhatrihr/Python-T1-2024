# n = int(input())

# matrix =[]
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j],end ='')

n = int(input())

matrix = [[
    '0' for _ in range(1, n+1)
] for _ in range(1, n+1)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = '1'

# print(matrix)

for row in matrix:
    # row = list(map(str, row))
    print(','.join(row))

# n = int(input())

# matrix = [[
#     '0' for _ in range(1, n+1)
# ] for _ in range(1, n+1)]

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             matrix[i][j] = '1'

# for row in matrix:
#     print(','.join(row))