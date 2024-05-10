# reg_number = input()
# print(reg_number)
# ans = 'TN07' in reg_number
# print(ans)

# AA00AA00
# TN07AA00
# AA00TN07
reg_number =input()
evidence ="TN07"
part_1 = reg_number[:4]
part_2 = reg_number[4:]
# print(part_1)
# print(part_2)
if part_1 == evidence or part_2 == evidence:
    print(True)
else:
    print(False)