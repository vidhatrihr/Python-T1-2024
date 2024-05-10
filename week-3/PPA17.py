a = input()
b = input()

new_word = ''
n = len(a) + len(b)

for i in range(n):
    new_digit = None
    
    if len(a) > 0 and len(b) > 0 and int(a[0]) < int(b[0]):
        new_digit = a[0]
        a = a[1:]
    elif len(a) > 0 and len(b) > 0 and int(b[0]) < int(a[0]):
        new_digit = b[0]
        b = b[1:]
    if new_digit is not None:
        new_word += new_digit
print(new_word + a + b)