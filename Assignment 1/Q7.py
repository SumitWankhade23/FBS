#Program to Find the Roots of a Quadratic Equation
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))

D = (b ** 2) - (4 * a * c)   # D = b² - 4ac

x1 = (-b + D ** 0.5) / (2 * a)   # D ** 0.5 = square root of D
x2 = (-b - D ** 0.5) / (2 * a)

print(f"\n  x1 = {x1:.2f}")
print(f"  x2 = {x2:.2f}")