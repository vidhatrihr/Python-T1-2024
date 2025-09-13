side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

#sum of leng of 2 side is greater than 3rd side

sum_1 = side_1 + side_2 
sum_2 = side_1 + side_3 
sum_3 = side_2 + side_3 

if sum_1 > side_3 and sum_2 > side_2 and sum_3 > side_1:
    print("YES")
else:
    print("NO")