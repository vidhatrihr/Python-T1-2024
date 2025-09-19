start = input()
end = input()

y1 = int(start[1])
y2 = int(end[1])

map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
}

x1 = map[start[0]]
x2 = map[end[0]]

if abs(x1-x2) == abs(y1-y2):
  print('YES')
else:
  print('NO')
