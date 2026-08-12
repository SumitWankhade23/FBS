#WAP to check if a given number is prime number or not.
n = int(input("Enter number: "))
for i in range(2,n):
    if( n%i == 0):
        print(n, "is not prime number")
        break
else:
    print(n, "is prime number")
