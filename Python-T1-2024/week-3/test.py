n = input()

max_dig = 0
for digit in n:
    digit = int(digit)
    if digit > max_dig:
        max_dig = digit
print(max_dig)