#Write a program to swap two numbers using third variable.

x = int(input("Enter number in x variable: "))
y = int(input("Enter number in y variable: "))


temp = x 
x = y 
y = temp
print("x =",x)
print("y =",y)