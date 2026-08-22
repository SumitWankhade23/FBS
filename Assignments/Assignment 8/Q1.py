#1. Write a program to calculate area of rectangle
def areaRectangle(l,b):
    area = l * b
    return area

l = float(input("Enter lenghth: "))
b = float(input("Enter breadth: "))
result = areaRectangle(l,b)
print(f"Area of rectangle = {result}")