email = str(input())

# branch_degree_year_roll@student.onlinedegree.institute.ac.in

branch = email[0:2]
degree = email[3:5]
year = email[6:8]
roll_number = email[9:13]
institute = email[35:39]

print(branch)
print(degree)
print(year)
print(roll_number)
print(institute)
