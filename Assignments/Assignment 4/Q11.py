#WAP to check if given number Strong Number.
num = int(input("Enter number: "))
n = num
sum = 0
while(num > 0):
    digit = num % 10

    fact = 1
    for i in range(1,digit+1):
        fact = fact * i

    sum = sum + fact
    num = num // 10
if(sum == n):
    print(f"{sum} is strong number") 
else:
    print(f"{n} - is not strong number ")       
