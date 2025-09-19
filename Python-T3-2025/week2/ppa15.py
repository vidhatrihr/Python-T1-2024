num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if num1 > num2:
  num1, num2 = num2, num1

if num2 > num3:
  num2, num3 = num3, num2

if num3 > num4:
  num3, num4 = num4, num3

print(num1, num2, num3, num4)
