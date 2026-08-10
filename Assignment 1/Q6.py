print("""      
Write a Program to input two angles from user and find third angle of the triangle.
      """)
A1 = float(input("Enter first angle: "))
A2 = float(input("Enter second angle : "))

Third_Angle = 180 - (A1 + A2)

print("Third angle: ", Third_Angle)
