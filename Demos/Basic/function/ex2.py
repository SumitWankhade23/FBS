def rectangle(l,b):
    A = l * b

    return A

l = int(input("Enter length: "))
b = int(input("Enter breadth."))
result = rectangle(l,b)
print(f"Area of rectangle: {result}")