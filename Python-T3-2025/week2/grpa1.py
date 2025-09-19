side1 = int(input())
side2 = int(input())
side3 = int(input())

if side3 == int((side1 ** 2 + side2 ** 2) ** 0.5) and side2 == int((side1 ** 2 + side3 ** 2) ** 0.5) and side1 == int((side3 ** 2 + side2 ** 2) ** 0.5):
  print('YES')
else:
  print('NO')
