# integers = list(map(int,input().split(',')))

# # max = 0
# max = (integers[0])
# for i in integers:
#     # integers[i] = int(integers[i])
#     if i > max:
#         max = i
# print(max)

n = list(map(int, input().split(',')))

max = int(n[0])
for num in n:
    if num > max:
        max = num
print(max)