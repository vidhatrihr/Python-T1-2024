# 1st person
p1_name = input()
p1_dob = input()

# 2nd person
p2_name = input()
p2_dob = input()

p1_date = int(p1_dob[:2])
p2_date = int(p2_dob[:2])

p1_month = int(p1_dob[3:5])
p2_month = int(p2_dob[3:5])

p1_year = int(p1_dob[-4:])
p2_year = int(p2_dob[-4:])

if p1_year > p2_year:
    print(p1_name)
if p1_year == p2_year and p1_month > p2_month:
    print(p1_name)
if p1_year == p2_year and p1_month == p2_month and p1_date > p2_date:
    print(p1_name)    

if p1_year < p2_year:
    print(p2_name)
if p1_year == p2_year and p1_month < p2_month:
    print(p2_name)
if p1_year == p2_year and p1_month == p2_month and p1_date < p2_date:
    print(p2_name)

if p1_year == p2_year and p1_month == p2_month and p1_date == p2_date:
    if p1_name.lower() < p2_name.lower():
        print(p1_name)
    else:
        print(p2_name)

# if int(p2_dob[:2]) > int(p1_dob[:2]) and int(p2_dob[3:5]) \
#     > int(p1_dob[3:5]) or int(p2_dob[6:]) > int(p1_dob[6:]):
#     print(p1_name)
# else:
#     print(p2_name)

# if p1_name.title() > p2_name.title():
#     print(p1_name)
# else:
#     print(p2_name)