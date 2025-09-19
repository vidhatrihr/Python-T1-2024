word = str(input())

vowels = ['a', 'e', 'i', 'o', 'u']
word = word.lower()

vowels_in_word = []

for vowel in vowels:
  if vowel in word:
    vowels_in_word += vowel

if vowels_in_word != []:
  vowels_in_word.sort()
  vowels_in_word = "".join(vowels_in_word)
  print(vowels_in_word)
