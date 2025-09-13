n = input()
digit = '0123456789.'

is_number = True


for num in n:
  if num  not in digit:
        is_number = False

if not is_number or n.count('.') > 1:
    print('None')
else:
    if '.' in n:
        print('Float')
    else:
        print('Integer')
