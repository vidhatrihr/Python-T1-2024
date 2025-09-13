no_of_coins = int(input())

share_1 = int(input())
share_2 = int(input())
share_3 = int(input())

# if  share_1 <= 0 and share_2 <= 0 and share_3 <= 0:
#     # if share_1 == share_2 == share_3:# this conditin is not working
#         if share_1 == share_2 or share_2 == share_3 or share_3 == share_1:
#            if share_1 + share_2 + share_3 == no_of_coins:
#                   print('unfair')
# else:
#     print('fair')


# to get non zero share_1
unfair_condition_1 = share_1 == 0 or share_2 == 0 or share_3 == 0

# no to shares must be eqaul
unfair_condition_2 = share_1 == share_2 or share_1 == share_3 or share_2 == share_3

# no coins left after sharing
unfair_condition_3 = share_1 + share_2 + share_3 != no_of_coins

if unfair_condition_1 or unfair_condition_2 or unfair_condition_3:
    print('UNFAIR')
else:
    print('FAIR')