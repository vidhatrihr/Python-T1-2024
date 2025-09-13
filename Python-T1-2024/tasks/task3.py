n = int(input())

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append('0')
    matrix.append(row)
# print(matrix)

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = '1'
# print(matrix)
for row in matrix:
    print(', '.join(row))