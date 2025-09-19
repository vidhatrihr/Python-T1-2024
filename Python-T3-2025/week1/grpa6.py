num1 = int(input())
num2 = int(input())


difference = 0

if num1 > num2:
  for num in range(num1):
    if num == 0:
      difference = num1 - num2
    else:
      if difference >= num2:
        difference -= num2
  print(difference)
else:
  print(num1)
