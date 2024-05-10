# original_word = input()


# if len(original_word) % 2 == 0:
#     if original_word[-1] == '.':
#         word = original_word / 10
#     else:
#         word = original_word + '.'
# # I took help here
#         mid = len(word) % 2 == 0
#     out = word[mid - 1 : mid + 2]
#     print(out)

word = input()
n = len(word)

if n % 2 == 0:
    if word[-1] == '.':
        word = word[:-1]
        n -= 1
    else:
        word = word +'.'
        n += 1

left = (n - 3)// 2
print(word[:left])
print(word[left:left + 3])
print(word[left + 3:])
