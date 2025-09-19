word = str(input())
gap = 0

if len(word) % 2 != 0:
  if word[-1] == '.':
    word = word[:-1]
  else:
    word = word + '.'
  gap = (len(word)-2)//2
else:
  gap = (len(word)-3)//2

# gap = int((len(word)-3)/2)
print(word[gap:gap+3])
# print(len("peter piper picked a peck of pickled peppers."))
