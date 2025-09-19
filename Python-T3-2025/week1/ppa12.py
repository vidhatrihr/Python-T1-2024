word = str(input())
start = int(input())
end = int(input())

new_word = ''
while (len(word) >= len(new_word)):
  new_word += word[start:end]
print(new_word)
