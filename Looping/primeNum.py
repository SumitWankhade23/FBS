n = int(input("Enter number: "))
for i in range(2,n):
    print(n)
    if (n%i == 0):
        print(f"{n} is not prime number ")
        break
else:
    print(f"{n} is prime number")    
   