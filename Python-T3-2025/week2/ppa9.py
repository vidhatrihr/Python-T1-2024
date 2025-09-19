coins = int(input())
share1 = int(input())
share2 = int(input())
share3 = int(input())

if share1 + share2 + share3 == coins and share1 != share2 != share3 != 0:
  print('FAIR')
else:
  print('UNFAIR')
