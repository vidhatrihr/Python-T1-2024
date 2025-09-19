from datetime import datetime

name1 = str(input())
dob1 = str(input())
name2 = str(input())
dob2 = str(input())

# DD-MM-YYYY
# dob1 = datetime(int(dob1[6:]), int(dob1[3:5]), int(dob1[0:2]))
# dob2 = datetime(int(dob2[6:]), int(dob2[3:5]), int(dob2[0:2]))

dob1 = datetime.strptime(dob1, "%d-%m-%Y")
dob2 = datetime.strptime(dob2, "%d-%m-%Y")

if dob1 > dob2:
  print(name1)
elif dob1 < dob2:
  print(name2)
elif name1 > name2:
  print(name2)
elif name1 < name2:
  print(name1)
