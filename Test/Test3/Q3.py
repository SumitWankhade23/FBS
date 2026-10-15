# 3. Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.
n = float(input("Enter salary: "))
if n < 20000:
    insent = n * (0.10 + 0.12 + 0.15)
    total_sal = insent + n
    print(total_sal)
else:
    insent = n * (0.15 + 0.18 + 0.20)
    total_sal = insent + n
    print(total_sal)    
