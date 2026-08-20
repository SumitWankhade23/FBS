#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter number"))
a = num % 10
x = num // 10
b = x % 10
c = x // 10

Rev = (a * 100) + (b * 10) + c

if( num == Rev):
    print(f"{num} is Palindrom number")
else:
    print(f"{num} is not Palindrom number")