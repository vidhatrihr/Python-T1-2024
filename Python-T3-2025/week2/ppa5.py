x1 = int(input())
y1 = int(input())
x2 = float(input())
y2 = float(input())
x = float(input())


if x2 - x1 != 0:
  slope = (y2 - y1) / (x2 - x1)
  y = (x - x1) / (x2 - x1) * (y2 - y1) + y1
  print(y)

  if slope == 0:
    print('horizontal Line')
  elif slope > 0:
    print('Positive Slope')
  else:
    print('Negative Slope')
else:
  print('Vertical Line')
