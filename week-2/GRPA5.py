password = input()
cond_1 = len(password) >= 8 and len(password) <= 32 
cond_2 = 'a' <= password[0] <= 'z' or 'A' <= password[0] <= 'Z'
cond_3 = '/' not in password and '\\' not in password and '=' not in password \
          and "'" not in password and '"' not in password and ' ' not in password

if cond_1 and cond_2 and cond_3:
    print(True)
else:
    print(False)