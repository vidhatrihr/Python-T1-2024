# word = input()
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# min_len = 0

# while word != alpha:
#     if len(word) < min_len:
#         min_len == word
#     word = input()
#     print(word)


min_len = float('inf')
while True:
    word = input()
    if word == 'abcdefghijklmnopqrstuvwxyz':
        break
    if len(word) < min_len:
        min_len = len(word)
        min_word = word
        
print(min_word)
    