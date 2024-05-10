# phone_no = input()

# if phone_no[0] == 6 or phone_no[0] == 7 or phone_no[0] == 8 or phone_no[0] == 9:
#     if len(phone_no) == 10:
#         for i in phone_no:
#             if len(i) < 7:

phone_no = input()

is_valid = True

if int(phone_no[0]) not in [6, 7, 8, 9]:
    is_valid = False


if len(phone_no) != 10:
    is_valid = False


for i in range(0, 10):
    if phone_no.count(str(i)) > 7 or phone_no.count(str(i)*5) > 0:
        is_valid = False
    

if is_valid:
    print('valid')
else:
    print('invalid')
