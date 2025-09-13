n = int(input())

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        element = str(i*3+j+1)
        row.append(element)
    matrix.append(row)
for row in matrix:
    print(','.join(row))
# print(','.join(matr))