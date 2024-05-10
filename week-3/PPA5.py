# n = int(input())
# max_in_n = n
# while n != 0:
#     if n > max_in_n:
#         max_in_n == n
#     n = int(input())
# print(max_in_n)


max = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n > max:
        max = n

print(max)