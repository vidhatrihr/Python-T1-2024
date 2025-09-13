words = input().split(',')

freq = {}

for word in words:
    if word not in freq:
        freq[word] = 0
    freq[word] += 1

# print(freq)