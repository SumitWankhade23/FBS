#Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
n = int(input("Enter number: "))
total = 0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact * j
    else:
        total += fact
print(f"Sum of series: {total}")            