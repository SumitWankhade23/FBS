#1.Write a program to check if the given number is positive or negative.
n = int(input("Enter number: "))
if( n > 0):
    print(f"{n} is positive number")
elif( n < 0):
    print(f"{n} is negative number")
else:
    print(f"Enetred number is zero")        