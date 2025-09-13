# number = input()

# if number == int(number):
#     print(number)
# if number != int(number):
#     if number > 0:
#         if number < 0:
x = float(input())

integer_part_of_x = int(x)
if integer_part_of_x == x:
    print(x) #floor
    print(x)#ceil

    # cas2
elif integer_part_of_x > 0:
    print(integer_part_of_x) # floor
    print(integer_part_of_x + 1)

# cas3
else:
    print(integer_part_of_x - 1) #floor
    print(integer_part_of_x) # ceil 