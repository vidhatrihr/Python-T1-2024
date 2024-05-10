L = input().split(',')

out = []

for i in L:
    out = [i] + out

n = len(out)

# for num in range(n-1):
#     print(out[num],end =',') # this is to print print all elem except last
# print(out[-1])  #this is to avoid comma at the end
print(','.join(out))


L = input().split(',')

out = []

for i in L:
    out = [i] + out
n = len(out)

print(','.join(out))

# list = input().split(',')

# reverse= []

# for i in list:
#     reverse = [i] + reverse

# print(','.join(reverse))