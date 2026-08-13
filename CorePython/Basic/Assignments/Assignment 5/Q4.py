#WAP to print Armstrong number within a given range
num = int(input("Enter number: "))
n = num
total = 0
count = 0

while (n > 0):
    count += 1
    n = n//10
n = num
while(n > 0):
    total = total + (n%10)**count
    n = n // 10

if( num == total):
    print(f"{num} is Armstrong number")
else:
    print(f"Is not Armstrong number")    