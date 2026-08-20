#Find the sum of three-digit number
num = int(input("Enter number"))
a = num % 10 
x = num // 10
b = x % 10
c = x // 10

total = a + b + c
print(f"Sum of three digit: {total}")