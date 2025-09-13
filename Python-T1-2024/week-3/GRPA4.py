# word = input().lower()

# output_let = ''
# len = len(word)
# alpha = 'abcdefghijklmnopqrstuvwxyz'

# for letter in alpha:
#     for i in range(0, len):
#         if letter == word[i]:
#             output_let += letter
# print(output_let)

word = input().lower()

alpha = 'abcdefghijklpmnopqrstuvwxyz'
output = ''

for letter in alpha:
    for i in range(0, len(word)):
        if letter == word[i]:
            output += letter

print(output)