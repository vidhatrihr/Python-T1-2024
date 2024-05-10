word = input()

all_vowel = 'a' in word and 'e' in word and 'i' in word  \
    and 'o' in word and 'u' in word
first_vowel_app_con = False
no_of_apper = False 

if all_vowel:
    first_vowel_app_con = word.index('a') < word.index('e')  \
    < word.index('i') < word.index('o') < word.index('u')

    no_of_apper = word.count('a') >=  word.count('e') >= word.count('i') \
    >= word.count('o') >= word.count('u')

if all_vowel and first_vowel_app_con and no_of_apper:
    print('It is a perfect word')
else:
    print('It is not a perfect word')
