# Team A
teamA_inning_1 = int(input())
teamA_wicket_lost_1 = int(input())
teamA_inning_2 = int(input())
teamA_wicket_lost_2 = int(input())

# Team B
teamB_inning_1 = int(input())
teamB_wicket_lost_1 = int(input())
teamB_inning_2 = int(input())
teamB_wicket_lost_2 = int(input())

score_sum_teamA = teamA_inning_1 + teamA_inning_2
score_sum_teamB = teamB_inning_1 + teamB_inning_2

if score_sum_teamA > score_sum_teamB and teamB_wicket_lost_2 == 10:
  print("Team A")
elif score_sum_teamA < score_sum_teamB:
  print('Team B')
elif score_sum_teamA == score_sum_teamB or teamB_wicket_lost_2 != 10:
  print("DRAW")
