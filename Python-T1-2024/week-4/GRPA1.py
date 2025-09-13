words = input().split()

word = input()

if word not in words:
    print('NO')

else:
    print('YES')
    print(words.count(word))