# 3. A list contains sublist with Emp information as follows :
# Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
# [210,”Tannu”,14000],[320,”Suresh”,35000]]
# Write a program to sort the list based on salary.
Data = [[101, "Seema", 45000], [340, "Rajani", 13000],
        [210, "Tannu", 14000], [320, "Suresh", 35000]]

Data.sort(key=lambda emp: emp[2])      

for emp in Data:
    print(emp)
