n = int(input())

mat_1 = [
    [int(x) for x in input().split(',')]
      for _ in range(n)]

mat_2 = [
    [int(x) for x in input().split(',')]
      for _ in range(n)]

product = []

for i in range(n):
    row = []
for j in range(n):
    for k in range(n):
        matrix = mat_1[i][k] * mat_2[k][j]
        row.append(str(matrix))

    product.append(','.join(row))

print(product)
