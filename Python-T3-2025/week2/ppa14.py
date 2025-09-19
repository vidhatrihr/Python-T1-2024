word = str(input())

vowels = {
    'a': 'e',
    'e': 'i',
    'i': 'o',
    'u': '',
}

perfect_word = False

for vowel, next_vowel in vowels.items():
  if vowel in word and next_vowel in word:
    if word.index(vowel) <= word.index(next_vowel):
      if word.count(vowel) >= word.count(next_vowel):
        perfect_word = True
      else:
        break
    else:
      break
  else:
    break

if perfect_word:
  print("It is a perfect word")
else:
  print('It is not a perfect word')
