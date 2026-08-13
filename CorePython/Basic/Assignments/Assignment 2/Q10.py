#Write a program to reverse three-digit number.
num = int(input("Enter number: "))
a = num % 10
x = num // 10
b = x % 10
c = x // 10

rev = (a*100) + (b*10) + c
print(f"Reverse number: {rev}")
