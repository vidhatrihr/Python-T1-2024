numbers = input().split(' ')
# print(numbers)

# k = []

for number in numbers[:-1]:
    print(int(float(number)), end=',')
    # k.append(str(int(float(number))))    
# print(','.join(k))
print(int(float(numbers[-1])))

# n = input().split()

# for number in n[:-1]:
#     print(int(float(number)),end=',')
# print(int(float(n[-1])))