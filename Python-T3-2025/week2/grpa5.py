password = str(input())

is_good = False
forbidden = {"/", "\"", "=", "'", '"'}

if len(password) >= 8 and len(password) <= 32:
  if not any(char in password for char in forbidden):
    if not password[0].isdigit():
      is_good = True

print(is_good)
