n = input()
# i = 0
# while len(n) > 0:
#     print(i)
#     if i > len(n)-1:
#         break
#     sum = n[i]
#     i += 1

sum = 0

for digit in n:
    digit = int(digit)
    sum += digit
print(sum)