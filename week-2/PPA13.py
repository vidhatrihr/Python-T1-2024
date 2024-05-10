ta_score_1 =  int(input())
ta_wicket_1 =int(input())
ta_score_2 =int(input())
ta_wicket_2 =int(input())
tb_score_1 =int(input())
tb_wicket_1 =int(input())
tb_score_2 =int(input())
tb_wicket_2 =int(input())

 
sum_Team_a =  ta_score_1 + ta_score_2 
sum_Team_b = tb_score_1 + tb_score_2 



if sum_Team_a > sum_Team_b and tb_wicket_2 == 10:
    print('Team A')
elif sum_Team_b > sum_Team_a:
    print('Team B')
elif sum_Team_a == sum_Team_b or tb_wicket_2 != 10:
    print('DRAW')
