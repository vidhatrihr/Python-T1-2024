input = int(input())

# print([int(digit) for digit in str(input)])

numbers = list(map(int, str(input)))

result = 0
for num in numbers:
  result += num

print(result)
