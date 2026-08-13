# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter number: "))
term = 1
total = 0
for i in range(1,n+1):
    total = total + term
    term = term * 2
print(f"Sum of series = {total}")    