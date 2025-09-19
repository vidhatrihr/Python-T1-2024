id1 = int(input())
id2 = int(input())
id3 = int(input())
id4 = int(input())
id5 = int(input())

ids = [id1, id2, id3, id4, id5]

even_seating = False

for index in range(len(ids)-1):
  if ids[index] + ids[index+1] % 2 == 0:
    even_seating = True

if even_seating:
  print('YES')
else:
  print('NO')
