word = input()
n = len(word)
half = (n-1) // 2
if n % 2 == 0:
      half += 1

is_palindrome = True

for i in range(n):
    if  i == half:
        break
    if not word[i] == word[n-i-1]:
        is_palindrome = False

if is_palindrome:
        print("PALINDROME")
else:
        print("NOT PALINDROME")