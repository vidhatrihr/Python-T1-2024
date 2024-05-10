marks = int(input())
no_of_opt = int(input())
correct_opt = list(map(int, input().split(',')))
choosen_opt = list(map(int, input().split(',')))
# print(marks)
# print(no_of_opt)
# print(correct_opt)
# print(choosen_opt)

marks_obtain = 0
wrong_opt_selected = False

for opt in choosen_opt:
    if opt in correct_opt:
        marks_obtain += marks / len(correct_opt)
    else:
        wrong_opt_selected = True

if wrong_opt_selected:
    print(0.0)
else:
    print(marks_obtain)
