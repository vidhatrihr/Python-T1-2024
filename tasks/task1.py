numbers = list(map(float, input().split()))

k = [int(element) ** 2 for element in numbers]

# for element in numbers:
#     element = element ** 2
#     k.append(element)

print(k)
