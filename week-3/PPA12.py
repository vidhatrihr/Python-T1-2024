string_1 = input()
string_2 = input()
new_string = ''

for letter in string_2:
    if letter in string_1:
     continue
    new_string += letter
print(new_string)