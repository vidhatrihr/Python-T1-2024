input = list(input())

for elem in input:
  if elem == ',':
    input.remove(',')

numbers = list(map(int, input))

product = 1
for x in range(len(numbers)):
  product *= numbers[x]

print(product)
