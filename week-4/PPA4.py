# L = []
# long = 0

# for i in L:
#     if L[len(i)] > long:
#         long = L[i]
# print(long)

max_word = '' # v r using this inverted comma becos this is not suppose to be input
max_len = 0

# input_list = input().split(',')
L = input().split(',')

for word in L:
    if len(word) >= max_len:
        max_len = len(word)
        max_word = word
print(max_word)


# max = 0
# max_word = ''
# for word in L:
#     if len(word) > max:
#         max = len(word)
#         max_word = word
# print(max)
