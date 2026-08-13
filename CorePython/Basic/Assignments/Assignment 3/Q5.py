#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = float(input("Enter side1: "))
b = float(input("Enter side2: "))
c = float(input("Enter side3: "))

if( a == b and b == c):
    print(f"Equilateral triangle")
elif( a ==b or a == b or b == c):
    print(f"Isoceles triangle") 
else:
    print(f"Scalene triangle")
           